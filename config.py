#default config
import os
class BaseConfig(object):
	DEBUG=False
	secret_key="my_precious"
	SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL']
    #HerokuPostgres :postgres://sbwuctsbjybzyy:EpSAZfsMb9r_R5WAhxpN3L1eev@ec2-54-83-201-196.compute-1.amazonaws.com:5432/de7fvp7mcfmuqp
	#(LOCAL MACHINE db)'postgresql:///tweetmin'
	#for mysql :'mysql://root:eashanrocks@localhost/posts'
	print SQLALCHEMY_DATABASE_URI

class DevelopmentConfig(BaseConfig):
	DEBUG=True