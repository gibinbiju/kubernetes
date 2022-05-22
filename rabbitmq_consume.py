import pika,json,time,sys

def main():
    try:
        with open(sys.argv[1]) as f:
            data = json.load(f)
        host = data.get("host","localhost")
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        def callback(ch, method, properties, body):
            try:
                print(body)
                ch.basic_ack(delivery_tag=method.delivery_tag)
                time.sleep(1)
            except:
                channel.close()

        channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=False)
        channel.basic_qos(prefetch_count=1)
        channel.start_consuming()
    except Exception as e:
        print(e)
        return 1
      
if __name__=='__main__':
    main()