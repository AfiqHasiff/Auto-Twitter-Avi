## Auto-Twitter-Avi

> Automated Twitter profile picture updater

## About The Project

If you have been a Twitter user since the dawn of time, I'm pretty sure you have seen users with GIFs as their avatar. As of 2013, Twitter has removed the ability to have animated GIFs as you profile picture, even though we are is still allowed to use GIFs as our profile picture, however <a href="https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_image#parameters">GIFs will be converted to a static GIF of the first frame, removing the animation.</a>

Regretting my decision for replacing my GIF profile picture with a more updated image for "cool points", this is the closest way I came up with to curb my regret.

## Prerequisites

### 1. Twitter developer account

Theres really no other way to have this automated easily without using APIs. I know what you're thinking, this sounds complicated. Uhm yes a bit for beginners BUT its really not that hard. Head over <a href="https://developer.twitter.com/en/apply-for-access">here</a> to get started. Once thats done, if Twitter requires more information on why you need a developer account they'll send you an email and all you have to do is state your intentions.

Next, you're going to have to enable **Read and Write** permission for your Twitter App at your project's permissions settings. If you've generated keys and tokens before enabling this permission, you **HAVE** to regenerate them if not you'll get a <a href="https://developer.twitter.com/en/support/twitter-api/error-troubleshooting">403 error</a> thrown at you.

### 2. Python dependencies

Run the command below in your terminal to install the required dependencies:
```sh
pip install -r requirements.txt
```
### 3. Config file
```sh
[Credentials]
api_key = q
api_secret = x
access_token = y
access_token_secret = z

[Upload_Interval]
interval = 60
```
Config file fields:

* **api_key**               - Consumer key obtained from Project Dashboard on your Twitter Developer Portal
* **api_secret**            - Consumer key obtained from Project Dashboard on your Twitter Developer Portal
* **access_token**          - Authentication token obtained from Project Dashboard on your Twitter Developer Portal
* **access_token**          - Authentication token obtained from Project Dashboard on your Twitter Developer Portal
* **access_token_secret**   - Authentication token obtained from Project Dashboard on your Twitter Developer Portal
* **interval**              - Time in minutes between each image upload. Only accepts integers.

### 4. Images

Place your soon-to-be profile pictures in `images/` directory. Image files allowed for Twitter profile pictures are `.png`, `.jpg`, `.jpeg` and `.gif` file types. Max image size allowed is **700kb** (_yes it's small dont ask me why, ask Twitter_). Unsupported file types and images larger than 700kb in the directory will be skipped by the program.

## Usage

### Start/Run

Really nothing special needed for now as it's still fairly basic. More coming soon tho.
```sh
python AviChanger.py
```

### Docker

Coming soon 👀

## Contact

* **Email** : ah.afiq.hasif@gmail.com
* **Instagram** : <a href="https://www.instagram.com/afiqhasiff/">AfiqHasiff</a>
