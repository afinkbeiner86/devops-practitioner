import requests
import smtplib
import os
import paramiko
import linode_api4
import time
import schedule

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')

def send_notification(email_message):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ethlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"{email_message}\n{response.status_code}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)

def restart_container(container_name, hostname):
    while True:
        client = linode_api4.LinodeClient(LINODE_TOKEN)
        linode_server = client.load(linode_api4.Instance, "mylinodeserver")
        if linode_server.status == 'running':
            time.sleep(5)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=hostname, username='root', key_filename='id_rsa')
            stdout = ssh.exec_command(f'docker start {container_name}')
            print(stdout.readlines())
            ssh.close()
        break

def restart_linode_server(hostname):
    client = linode_api4.LinodeClient(LINODE_TOKEN)
    linode_server = client.load(linode_api4.Instance, hostname)
    linode_server.reboot()

def monitor_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'Website is running.\nStatusCode: {response.status_code}\n')
        else:
            print(f'Error: Website is not running\nStatusCode: {response.status_code}\n')
            send_notification("THE WEBSITE IS DOWN!")

            # try to restart web app
            restart_container("nginx", "mywebserver")

    except Exception as ex:
        print(f'Connection error: {ex}')
        send_notification("Application not running.")

        # try to restart linode server
        restart_linode_server("mylinodeserver")

        # restart container
        restart_container("nginx", "mywebserver")

schedule.every(5).minutes.do(monitor_website("http://mywebsite:8080"))

while True:
    schedule.run_pending()