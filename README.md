# Python Boilerplate

This is a project intended for use as a general setup when trying to build a Python integration using Google App Engine and Google Actions.

Only very basic configuration is applied. For now it is a simple Flask server being deployed.

Currently, envfile is built during a github actions step, so relevant envfiles should be created as secrets on the repository.

(NOTE: Github actions must be enabled and the proper secrets / GCloud configurations must be done)

## AppEngine Setup

* Create Service Account (SA)
  - Create credentials file and save as a secret on Github Actions
  - Also set project name on secrets
  - Pass the service account name as variable (TODO fix)
* Set up SA roles:
  * App Engine Deployer
  * App Engine Service Admin
  * Cloud Build Service Account
  * Service Account User (Overrides default SA)
  * Storage Object Creator
  * Storage Object Viewer

If everything is set up correctly, deployment should be done automatically to the specified App Engine project.