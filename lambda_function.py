import boto3
import os

def lambda_handler(event, context):
    ses_client = boto3.client('ses', region_name='us-east-1')

    sender_email = "your-verified-email@example.com"
    recipient_email = "viniciuscamacho12@gmail.com"
    subject = "Test Email from AWS Lambda"
    body_text = "This is a test email sent from an AWS Lambda function."
    body_html = """<html>
    <head></head>
    <body>
      <h1>Test Email from AWS Lambda</h1>
      <p>This is a test email sent from an AWS Lambda function.</p>
    </body>
    </html>"""

    try:
        response = ses_client.send_email(
            Destination={
                'ToAddresses': [recipient_email],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': "UTF-8",
                        'Data': body_html,
                    },
                    'Text': {
                        'Charset': "UTF-8",
                        'Data': body_text,
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': subject,
                },
            },
            Source=sender_email,
        )
        return {
            'statusCode': 200,
            'body': 'Email sent!'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
