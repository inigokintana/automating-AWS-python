import boto3
#import sys
import click

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webtron deploys websites to AWS"
    pass

@click.command('list-buckets')
def list_buckets():
    "List all S3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@click.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
        "List object in an S3 bucket"
        for obj in s3.Bucket(bucket).objects.all():
            print(obj)

if __name__ == "__main__":
#    print(sys.argv)
    cli()
