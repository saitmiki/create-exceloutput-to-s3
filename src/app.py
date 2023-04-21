import boto3
import openpyxl
import io

def lambda_handler(event, context):

    # Create a new workbook object
    workbook = openpyxl.Workbook()

    # Select the active worksheet
    worksheet = workbook.active

    # Write some data to the worksheet
    worksheet['A1'] = 'Hello'
    worksheet['B1'] = 'Customer!'

    # Save the workbook to a BytesIO object
    output = io.BytesIO()
    workbook.save(output)
    print(output)

    # Reset the file pointer to the beginning
    output.seek(0)

    # Create an S3 client
    s3 = boto3.client('s3')

    # Upload the workbook to S3
    res = s3.upload_fileobj(output, 'test-customers-saitmiki', 'customer-m/example.xlsx')
    print(res)

    return {
        'statusCode': 200,
        'body': 'Excel file created and uploaded to S3!'
    }
