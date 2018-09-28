from fabric.api import env, run, local, cd, sudo
    #env.host=["18.222.171.80"]
def update(comment):
    env.host_string="ec2-18-222-171-80.us-east-2.compute.amazonaws.com"
	env.user="ubuntu"
	env.key_filename = 'C:\\Program Files\\OpenSSH\\home\\Алексей\\.ssh\\weizmann.pem'
	local("git add .")
	local("git commit -a -m {}".format(str(comment))
	local("git push")
	with cd("/home/ubuntu/site"):
	    run("git pull")
		sudo("supervisorctl restart flask")
