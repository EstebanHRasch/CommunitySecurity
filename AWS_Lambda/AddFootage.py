import psycopg2


# This function has been modified to run a test script to insert specific video footage instances
# as the team cannot access the camera modules at the time. 
# AWS requires a compiled version of psycopg 2 to be uploaded, it should already be there.
def AddFootage(event, context):
    try:
        connection = psycopg2.connect( host="videofootage.cp9na604eeux.us-east-2.rds.amazonaws.com", user="snumata", password="communitysecurity", dbname="SurveilanceEC2" )
    
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")
        bucketPath = 'https://rasptest.s3.us-east-2.amazonaws.com/'
        #key = event['Records'][0]['s3']['object']['key']
        #url = bucketPath + key
        #url = "https://rasptest.s3.us-east-2.amazonaws.com/2020-03-04/17-14-37.mp4"
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        #if select exists(select 1 from polls_footage_time where pub_date = current_date)
        #cursor.execute('''INSERT INTO console_footage (date, "URL", camera_id) VALUES ("2020-04-28", "https://rasptest.s3.us-east-2.amazonaws.com/2020-03-04/17-14-37.mp4", 1)''');
        insert_stmt = ("INSERT INTO console_footage (date, \"URL\", camera_id, time, thumbnail) VALUES (%s, %s, 1, CURRENT_TIMESTAMP, %s)")
        data = ("2020-04-24", "https://rasptest.s3.us-east-2.amazonaws.com/2020-03-04/17-14-37.mp4", "From AWS Labmda");
        cursor.execute(insert_stmt, data)
       
        #record = cursor.fetchone()
        #print("You are connected to - ", record,"\n")
        connection.commit()
    
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")