import Flask

   app = Flask(__name__)

   @app.route(&#39;/&#39;)
   def hello_world():
      target = os.environ.get(&#39;TARGET&#39;, &#39;World&#39;)
      return &#39;Hello {}!\n&#39;.format(target)

   if __name__ == &#34;__main__&#34;:
      app.run(debug=True,host=&#39;0.0.0.0&#39;,port=int(os.environ.get(&#39;PORT&#39;, 8080)))
