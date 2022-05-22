import pika,json,sys

def main():
    try:
        with open(sys.argv[1]) as f:
            data = json.load(f)
        host = data.get("host","localhost")
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        print("connected to channel")

        for i in range(10):
            msg = json.dumps({"message":i})
            print(msg)
            channel.basic_publish(exchange='',
                            routing_key='hello',
                            body=msg)
    except Exception as e:
        channel.close()
        print(e)


if __name__=='__main__':
    print("start time")
    main()