# cos-test-python

## Start Allure web server

* Open Terminal and navigate to the project root

  ```commandline
  bash start_allure_server.sh
  ```

* If the server is error, run the command

  ```commandline
  bash reset_allure_server.sh
  ```

## Run tests

* Run only one test case

  ```commandline
  bash run.sh tests/user_management/test_create_new_team.py
  ```
