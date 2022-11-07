<main class="col-md" style="margin-bottom: 164px; margin-top: 0px;">

<a data-id="" id="learning-goals" style="top: 0px;"></a><h2><a data-id="" href="#learning-goals">Learning Goals</a></h2>
<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Build a simple flask app to gain an understanding of how to use this framework</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Become familiar with Jinja, a templating language used with Flask</li>
</ul>

<a data-id="" id="background" style="top: 0px;"></a><h2><a data-id="" href="#background">Background</a></h2>

<p><a href="https://flask.palletsprojects.com/">Flask</a>, a <a href="https://en.wikipedia.org/wiki/Microframework">microframework</a> used for web development, can be confusing when starting out. There are multiple files of different types, and they must reside in specific folders. In this problem, we’ll start with the absolute minimum—a single Python file. From there we will move on to create your first full-fledged web app!</p>

<a data-id="" id="getting-started" style="top: 0px;"></a><h2><a data-id="" href="#getting-started">Getting Started</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>Execute <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/9/helloflask.zip</code> followed by Enter in order to download a zip called <code class="language-plaintext highlighter-rouge">helloflask.zip</code> in your codespace. Take care not to overlook the space between <code class="language-plaintext highlighter-rouge">wget</code> and the following URL, or any other character for that matter!</li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">unzip helloflask.zip</code> to create a folder called <code class="language-plaintext highlighter-rouge">helloflask</code>.</li>
  <li>You no longer need the ZIP file, so you can execute <code class="language-plaintext highlighter-rouge">rm helloflask.zip</code> and respond with “y” followed by Enter at the prompt.</li>
  <li>Finally, right-click or control-click on the <code class="language-plaintext highlighter-rouge">helloflask</code> folder and click “Open in CS50 Lab”. You should see the specification for this problem on the left-hand side and its distribution code on the right-hand side.</li>
</ol>

<a data-id="" id="implementation-details" style="top: 0px;"></a><h2><a data-id="" href="#implementation-details">Implementation Details</a></h2>

<p>The most simple Flask app uses just one file, <code class="language-plaintext highlighter-rouge">app.py</code>. This will create an html page and say hello. Add the following into <code class="language-plaintext highlighter-rouge">app.py</code> to get started.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">Flask</span>

<span class="n">app</span> <span class="o">=</span> <span class="n">Flask</span><span class="p">(</span><span class="n">__name__</span><span class="p">)</span>


<span class="o">@</span><span class="n">app</span><span class="p">.</span><span class="n">route</span><span class="p">(</span><span class="s">"/"</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">index</span><span class="p">():</span>
    <span class="k">return</span> <span class="s">"Hello, World!"</span>
</code></pre></div></div>

<p>This bit of code starts by importing <code class="language-plaintext highlighter-rouge">Flask</code> from the <code class="language-plaintext highlighter-rouge">flask</code> library. Though we don’t need to get too far into the weeds here, <code class="language-plaintext highlighter-rouge">Flask</code> is what programmers call a “<a href="https://cs50.harvard.edu/python/2022/notes/8/#classes">class</a>”. Suffice to say for now, it’s like a template for the application we’ll be building. The line <code class="language-plaintext highlighter-rouge">app = Flask(__name__)</code> tells Python to create a particular app, henceforth called “app”, from the template. To create the particular application, we give the <code class="language-plaintext highlighter-rouge">Flask</code> class the name of the current Python file (represented by <code class="language-plaintext highlighter-rouge">__name__</code>), which allows our application to find other files we might later add to it. In this case, the name of the file is also “app” for consistency.</p>

<p>The most mysterious line in the application you’ve written is probably the one where you wrote:</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="o">@</span><span class="n">app</span><span class="p">.</span><span class="n">route</span><span class="p">(</span><span class="s">"/"</span><span class="p">)</span>
</code></pre></div></div>

<p>This kind of function is called a decorator. Decorators allow you to take a basic function, like <code class="language-plaintext highlighter-rouge">app.route</code>, and extend its functionality with something custom: the function you write after the decorator. You can <a href="https://realpython.com/primer-on-python-decorators/">read more</a> about decorators if you want, or you can just keep using them for now.</p>

<p>This line tells Flask that if an HTTP request comes in for “/”, the <code class="language-plaintext highlighter-rouge">index</code> function should be run. Note that, if we renamed the function to be <code class="language-plaintext highlighter-rouge">homepage</code>, this line would tell Flask that—every time it receives an HTTP request for “/”—it should run the <code class="language-plaintext highlighter-rouge">homepage</code> function.</p>

<p>Notice that the <code class="language-plaintext highlighter-rouge">index</code> function returns a piece of text, “Hello, World!”. This text is what Flask will render to the user when their request to the “/” route is complete. The returned text could be (and often is!) the text of n entire HTML file, which the browser then renders accordingly. But it’s just a piece of text for now, for brevity’s sake.</p>

<p>To run your app, type <code class="language-plaintext highlighter-rouge">flask run</code> into the terminal, and you will get a link to click, similar to when you run <code class="language-plaintext highlighter-rouge">http-server</code>. You’ve written a Flask app!  Try returning different text, like <code class="language-plaintext highlighter-rouge">&lt;h1&gt;Hello, World!&lt;/h1&gt;</code>. How does this change what you see?</p>

<a data-id="" id="templates" style="top: 0px;"></a><h3><a data-id="" href="#templates">Templates</a></h3>

<p>Instead of putting HTML code right into our Python programs, it’s best to move our HTML into separate files, to keep separate concerns separate. Since our app will likely include a number of similar HTML files, we can create one <code class="language-plaintext highlighter-rouge">layout.html</code> file which all our HTML files “extend”. “Extending” an HTML file means to keep all of the content of that HTML file while also adding some custom content, specific to a particular page.</p>

<p>By convention, Flask puts all HTML files inside of a <code class="language-plaintext highlighter-rouge">templates</code> folder. Inside the <code class="language-plaintext highlighter-rouge">helloflask</code> folder, make a folder called <code class="language-plaintext highlighter-rouge">templates</code> using <code class="language-plaintext highlighter-rouge">mkdir templates</code>. All your HTML files will go in this <code class="language-plaintext highlighter-rouge">templates</code> folder.</p>

<p>Inside <code class="language-plaintext highlighter-rouge">templates</code>, create a <code class="language-plaintext highlighter-rouge">layout.html</code> file that looks like this:</p>

<div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="cp">&lt;!DOCTYPE html&gt;</span>

<span class="nt">&lt;html</span> <span class="na">lang=</span><span class="s">"en"</span><span class="nt">&gt;</span>
    <span class="nt">&lt;head&gt;</span>
        <span class="nt">&lt;title&gt;</span>Hello, Flask<span class="nt">&lt;/title&gt;</span>
    <span class="nt">&lt;/head&gt;</span>
    <span class="nt">&lt;body&gt;</span>
        <span class="nt">&lt;h1&gt;</span>Hello, Flask<span class="nt">&lt;/h1&gt;</span>
        {% block body %}{% endblock %}
    <span class="nt">&lt;/body&gt;</span>
<span class="nt">&lt;/html&gt;</span>
</code></pre></div></div>

<p>The <code class="language-plaintext highlighter-rouge">{% block body %}{% endblock %}</code> syntax comes from <a href="https://palletsprojects.com/p/jinja/">Jinja</a>, which is a “template engine” for Python. The line with <code class="language-plaintext highlighter-rouge">{% block body %}{% endblock %}</code> is what makes this a layout file. If another HTML file extends <code class="language-plaintext highlighter-rouge">layout.html</code> and defines a block called “body”, we’ll insert that block into this section of the <code class="language-plaintext highlighter-rouge">layout.html</code>. A layout file can contain as many blocks as you want. Just give each one a different name.</p>

<p>Now create <code class="language-plaintext highlighter-rouge">index.html</code> so that it extends the template <code class="language-plaintext highlighter-rouge">layout.html</code>, like this:</p>

<div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><code>{% extends "layout.html" %}

{% block body %}
    <span class="nt">&lt;p&gt;</span>Next we'll put a form here and get some POST action!<span class="nt">&lt;/p&gt;</span>
{% endblock %}
</code></pre></div></div>

<p>Finally, we’ll go back to <code class="language-plaintext highlighter-rouge">app.py</code> to see these changes come to life. In the initial import, we’ll need a few more functions from Flask (as shown below). Then, replace the direct return of text with a call to Flask’s <code class="language-plaintext highlighter-rouge">render_template</code> function. The purpose of the <code class="language-plaintext highlighter-rouge">render_template</code> function is to preprocess <code class="language-plaintext highlighter-rouge">index.html</code> such that, when we give it to the browser, it also includes the HTML it “inherits” from <code class="language-plaintext highlighter-rouge">layout.html</code>.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">Flask</span><span class="p">,</span> <span class="n">render_template</span><span class="p">,</span> <span class="n">request</span>

<span class="n">app</span> <span class="o">=</span> <span class="n">Flask</span><span class="p">(</span><span class="n">__name__</span><span class="p">)</span>


<span class="o">@</span><span class="n">app</span><span class="p">.</span><span class="n">route</span><span class="p">(</span><span class="s">"/"</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">index</span><span class="p">():</span>
    <span class="k">return</span> <span class="n">render_template</span><span class="p">(</span><span class="s">"index.html"</span><span class="p">)</span>
</code></pre></div></div>

<p>When you run your application now (type <code class="language-plaintext highlighter-rouge">flask run</code>!), you’ll get a little more out of your app. But it isn’t really interactive yet!</p>

<a data-id="" id="forms" style="top: 0px;"></a><h3><a data-id="" href="#forms">Forms</a></h3>

<p>HTML forms allow the user to enter data into input fields and send the data to the server, often using the POST method of the HTTP protocol. You can learn more about HTML Forms <a href="https://www.w3schools.com/html/html_forms.asp">here</a>.</p>

<p>Add a form to <code class="language-plaintext highlighter-rouge">index.html</code> so that it looks like this:</p>

<div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><code>{% extends "layout.html" %}

{% block body %}
    <span class="nt">&lt;form</span> <span class="na">action=</span><span class="s">"/"</span> <span class="na">method=</span><span class="s">"post"</span><span class="nt">&gt;</span>
        What is your favorite color?
        <span class="nt">&lt;select</span> <span class="na">name=</span><span class="s">"color"</span><span class="nt">&gt;</span>
            <span class="nt">&lt;option</span> <span class="na">value=</span><span class="s">"red"</span><span class="nt">&gt;</span>Harvard Crimson<span class="nt">&lt;/option&gt;</span>
            <span class="nt">&lt;option</span> <span class="na">value=</span><span class="s">"blue"</span><span class="nt">&gt;</span>Yale Blue<span class="nt">&lt;/option&gt;</span>
        <span class="nt">&lt;/select&gt;</span>
        <span class="nt">&lt;button</span> <span class="na">type=</span><span class="s">"submit"</span><span class="nt">&gt;</span>Submit<span class="nt">&lt;/button&gt;</span>
    <span class="nt">&lt;/form&gt;</span>
{% endblock %}
</code></pre></div></div>

<p>Note that each form element has both a <em>name</em> and a <em>value</em>. The name an element is what we’ll use to refer to that element. Its value is the value submitted by the form. Each get passed into <code class="language-plaintext highlighter-rouge">app.py</code> for our use when the form is submitted.</p>

<p>Run your app, visit the <code class="language-plaintext highlighter-rouge">/</code> route, and submit the form. Oops! You should see the message “Method not allowed”. So we’ll first need to make sure Flask allows the use of the POST method on <code class="language-plaintext highlighter-rouge">/</code>.</p>

<a data-id="" id="post" style="top: 0px;"></a><h3><a data-id="" href="#post">POST</a></h3>

<p>In <code class="language-plaintext highlighter-rouge">app.py</code>, we need to adjust our route to handle the POST request. Here is what our new <code class="language-plaintext highlighter-rouge">app.py</code> looks like.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">Flask</span><span class="p">,</span> <span class="n">render_template</span><span class="p">,</span> <span class="n">request</span>

<span class="n">app</span> <span class="o">=</span> <span class="n">Flask</span><span class="p">(</span><span class="n">__name__</span><span class="p">)</span>


<span class="o">@</span><span class="n">app</span><span class="p">.</span><span class="n">route</span><span class="p">(</span><span class="s">"/"</span><span class="p">,</span> <span class="n">methods</span><span class="o">=</span><span class="p">[</span><span class="s">"GET"</span><span class="p">,</span> <span class="s">"POST"</span><span class="p">])</span>
<span class="k">def</span> <span class="nf">index</span><span class="p">():</span>
    <span class="k">if</span> <span class="n">request</span><span class="p">.</span><span class="n">method</span> <span class="o">==</span> <span class="s">"GET"</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">render_template</span><span class="p">(</span><span class="s">"index.html"</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">print</span><span class="p">(</span><span class="s">"Form submitted!"</span><span class="p">)</span>
        <span class="n">color</span> <span class="o">=</span> <span class="n">request</span><span class="p">.</span><span class="n">form</span><span class="p">.</span><span class="n">get</span><span class="p">(</span><span class="s">"color"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">render_template</span><span class="p">(</span><span class="s">"color.html"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="n">color</span><span class="p">)</span>
</code></pre></div></div>

<p>This example has some logic in it: if the user submits a GET request, we’ll show them the basic <code class="language-plaintext highlighter-rouge">index.html</code> with a form to submit. If, though, they submit a POST request, we’ll do a few different things:</p>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span><code class="language-plaintext highlighter-rouge">print</code> “Form submitted!” to the terminal, for debugging’s sake. We should later remove this once we’re satisfied our program works as intended.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Store the <em>value</em> of the “color” input in a variable also called <code class="language-plaintext highlighter-rouge">color</code>, as via <code class="language-plaintext highlighter-rouge">color = request.form.get("color")</code>.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Render a new HTML file, <code class="language-plaintext highlighter-rouge">color.html</code>, and pass the value of the <code class="language-plaintext highlighter-rouge">color</code> variable into the file under the very same name, <code class="language-plaintext highlighter-rouge">color</code>.</li>
</ul>

<p>Let’s create <code class="language-plaintext highlighter-rouge">color.html</code> for our application to work:</p>

<div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><code>{% extends "layout.html" %}

{% block body %}
    <span class="nt">&lt;p</span> <span class="na">style=</span><span class="s">"color: {{ color }}"</span><span class="nt">&gt;</span>Your favorite color is {{ color }}.<span class="nt">&lt;/p&gt;</span>
{% endblock %}
</code></pre></div></div>

<p>Notice how we can insert the value of <code class="language-plaintext highlighter-rouge">color</code> anywhere in our HTML we’d like—whether as text in a sentence, or as a placeholder for the value of some CSS property.</p>

<p>We’ll likely want to add some additional input validation, however, instead of simply trusting our users to send only the values “blue” or “red” via POST. What additional code could you add to ensure the colors we receive are valid colors?</p>

<a data-id="" id="how-to-test-your-code" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test-your-code">How to Test Your Code</a></h2>

<p>Your program should behave as per the examples above.</p>

<p>No <code class="language-plaintext highlighter-rouge">check50</code> for this one!</p>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit. This is a practice problem!</p>

<div class="alert alert-primary" data-alert="primary" role="alert"><p><em>Adapted from 27 Classrooms, by Mark Sobkowicz, Lincoln Sudbury Regional High School</em></p></div>
