# digital_ocean_dynamic_ip
Python script to update DNS records at Digital Ocean for a server with a dynamic IP address

# why
If you want to run a server at home, but don't have a static IP address, you can deploy this script on your server to keep the A records of your domain in sync with your dynamic IP

# how
- have Digital Ocean manage your domain records for the domain you want to use (it's free)
- Set the TTL for your a records to 300 (5 minutes)
- Create Digital Ocean personal access token with "write" capabilities (API > Tokens/keys)
- Copy the python script on your server
- Replace "YOUR_OAUTH_TOKEN" with your personal access token from Digital Ocean
- Replace "MYDOMAIN.COM" with your own top level domain
- Create a cron job (eg: */5 * * * * python /home/user/dynip.py > /var/logs/dynip/dynip) to run the script every 5 minutes
- You now have a server with a dynamic ip address that is accessable from the internet

# other notes
- This script updates all A records for teh domain, if you only need to update 1 record you'll need to edit the script
- In order for your server to be accessable from your dynamic ip you will need to configure DMZ or port forwarding on your router
