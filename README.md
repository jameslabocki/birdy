# Birdy

Birdy is an application written for Rasberry Pi that takes pictures when sensing motion and posts them to twitter. The application assumes that you have the following:

## Credentials
A credentials.py file in the local directory where birdy.py is being run that contains the following:

```
consumer_key = 'Your Twitter API Key'
consumer_secret = 'Your Twitter API Secret'
bearer_token = 'Your bearer token'
access_token = 'Your Twitter access token'
access_token_secret = 'Your Twitter Access Token Secret'
```


You will need to request enhanced privileges in your Twitter developer account in order for birdy to be able to write tweets. This can take some time to have it granted.

## Wiring
Birdy looks for the control wire from the PIR sensor to be on GPIO(27). 

It may be helpful to check out this [rasberry pi diagram](https://www.etechnophiles.com/wp-content/uploads/2021/01/Raspberry-Pi-4-GPIO-header.jpg?ezimgfmt=ng:webp/ngcb40) and also the schematic for the [HC-SR501](https://www.mpja.com/download/31227sc.pdf) PIR sensor. 


