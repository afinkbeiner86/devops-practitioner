# Module 3 - Build Tools & Package Manager Tools

#### "Build Tools, Package Managers"
Build a java application using gradle.

###### Build
```bash
./gradlew build
```

###### Run
```bash
java -tar ./build/lib/your-tar.tar
```


#### Exercises


</details>

******

<details>
<summary>Exercise 0: Clone project and create own Git repository </summary>
 <br />

**steps:**

```sh
# clone repository & change into project dir
git clone git@gitlab.com:devops-bootcamp3/java-gradle-app.git
cd java-gradle-app

# remove remote repo reference and create your own local repository
rm -rf .git
git init 
git add .
git commit -m "initial commit"

# create git repository on Gitlab and push your newly created local repository to it
git remote add origin git@gitlab.com:{gitlab-user}/{gitlab-repo}.git
git push -u origin master

```

</details>

******

<details>
<summary>Exercise 1: Build jar artifact </summary>
 <br />

**steps**

```sh
./gradlew build

```

</details>

******

<details>
<summary>Exercise 2: Run tests </summary>
 <br />

**steps:**
```sh
# locate AppTest.java file in src/test/java folder, line 22 & fix test
boolean result = myApp.getCondition(true); 

# run tests
./gradlew test

```

</details>

******

<details>
<summary>Exercise 3: Clean & build App </summary>
 <br />

**steps:**
```sh
./gradlew clean 
./gradlew build

```

</details>

******

<details>
<summary>Exercise 4: Start application </summary>
 <br />

**steps:**
```sh
java -jar bootcamp-java-project-1.0-SNAPSHOT.jar

```

</details>

******

<details>
<summary>Exercise 5: Start App with 2 Parameters </summary>
 <br />

**steps:**
```sh
# add parameter input to the Java code, in Application.java, on line 16
Logger log = LoggerFactory.getLogger(Application.class); 
try { 
    String one = args[0]; 
    String two = args[1]; 
    log.info("Application will start with the parameters {} and {}", one, two); 
} catch (Exception e) { 
    log.info("No parameters provided"); 
}

# rebuild the jar file 
./gradlew build

# run application with ANY 2 parameters
java -jar bootcamp-java-project-1.0-SNAPSHOT.jar myname mylastname

```

</details>
