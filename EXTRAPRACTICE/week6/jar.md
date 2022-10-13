<main class="col-md" style="margin-bottom: 265px; margin-top: 0px;">

<p>Suppose that you’d like to implement a <a href="https://en.wikipedia.org/wiki/Cookie_jar">cookie jar</a> in which to store cookies. In a file called <code class="language-plaintext highlighter-rouge">jar.py</code>, implement a <code class="language-plaintext highlighter-rouge">class</code> called <code class="language-plaintext highlighter-rouge">Jar</code> with these methods:</p>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span><code class="language-plaintext highlighter-rouge">__init__</code> should initialize a cookie jar with the given <code class="language-plaintext highlighter-rouge">capacity</code>, which represents the maximum number of cookies that can fit in the cookie jar. If <code class="language-plaintext highlighter-rouge">capacity</code> is not a non-negative <code class="language-plaintext highlighter-rouge">int</code>, though, <code class="language-plaintext highlighter-rouge">__init__</code> should instead raise a <code class="language-plaintext highlighter-rouge">ValueError</code> (via <code class="language-plaintext highlighter-rouge">raise ValueError</code>).</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span><code class="language-plaintext highlighter-rouge">__str__</code> should return a <code class="language-plaintext highlighter-rouge">str</code> with <mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="0" style="font-size: 113.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml></mjx-container> <code class="language-plaintext highlighter-rouge">🍪</code>, where <mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="1" style="font-size: 113.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml></mjx-container> is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then <code class="language-plaintext highlighter-rouge">str</code> should return <code class="language-plaintext highlighter-rouge">"🍪🍪🍪"</code></li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span><code class="language-plaintext highlighter-rouge">deposit</code> should add <code class="language-plaintext highlighter-rouge">n</code> cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, <code class="language-plaintext highlighter-rouge">deposit</code> should instead raise a <code class="language-plaintext highlighter-rouge">ValueError</code>.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span><code class="language-plaintext highlighter-rouge">withdraw</code> should remove <code class="language-plaintext highlighter-rouge">n</code> cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, <code class="language-plaintext highlighter-rouge">withdraw</code> should instead raise a <code class="language-plaintext highlighter-rouge">ValueError</code>.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span><code class="language-plaintext highlighter-rouge">capacity</code> should return the cookie jar’s capacity.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span><code class="language-plaintext highlighter-rouge">size</code> should return the number of cookies actually in the cookie jar.</li>
</ul>

<p>Structure your <code class="language-plaintext highlighter-rouge">class</code> per the below. You may not alter these methods’ parameters, but you may add your own methods.</p>

<div class="language-py highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">class</span> <span class="nc">Jar</span><span class="p">:</span>

    def __init__(self, capacity=12):
        ...

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
        
   
</code></pre></div></div>

<p>You’re welcome, but not required, to implement a <code class="language-plaintext highlighter-rouge">main</code> function in which to test your class, so this is all we can demo!</p>

<a data-id="" id="before-you-begin" style="top: 0px;"></a><h2><a data-id="" href="#before-you-begin">Before You Begin</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>Execute <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/6/jar.zip</code> followed by Enter in order to download a zip called <code class="language-plaintext highlighter-rouge">jar.zip</code> in your codespace. Take care not to overlook the space between <code class="language-plaintext highlighter-rouge">wget</code> and the following URL, or any other character for that matter!</li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">unzip jar.zip</code> to create a folder called <code class="language-plaintext highlighter-rouge">jar</code>.</li>
  <li>You no longer need the ZIP file, so you can execute <code class="language-plaintext highlighter-rouge">rm jar.zip</code> and respond with “y” followed by Enter at the prompt.</li>
  <li>Finally, right-click or control-click on the <code class="language-plaintext highlighter-rouge">jar</code> folder and click “Open in CS50 Lab”. You should see the specification for this problem on the left-hand side and its distribution code on the right-hand side.</li>
</ol>

<a data-id="" id="how-to-test" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test">How to Test</a></h2>

<p>Here’s how to test your code manually:</p>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Define a <code class="language-plaintext highlighter-rouge">main</code> function in your <code class="language-plaintext highlighter-rouge">jar.py</code> file, wherein you create a new instance of <code class="language-plaintext highlighter-rouge">Jar</code> with <code class="language-plaintext highlighter-rouge">jar = Jar()</code>. Test this <code class="language-plaintext highlighter-rouge">jar</code> has the capacity it should by calling <code class="language-plaintext highlighter-rouge">print(str(jar.capacity))</code>. Be sure your program calls <code class="language-plaintext highlighter-rouge">main</code> at the bottom of the file, as via <code class="language-plaintext highlighter-rouge">main()</code>.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Test that your <code class="language-plaintext highlighter-rouge">__str__</code> function works as intended by calling <code class="language-plaintext highlighter-rouge">print(str(jar))</code>.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Try calling <code class="language-plaintext highlighter-rouge">jar.deposit(2)</code> to deposit two cookies. Calling <code class="language-plaintext highlighter-rouge">print(str(jar))</code> should now show you the same number of cookies you’ve deposited.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Try calling <code class="language-plaintext highlighter-rouge">jar.withdraw(1)</code> to withdraw one cookie. Calling <code class="language-plaintext highlighter-rouge">print(str(jar))</code> should now show you one fewer cookie than you had before.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Try experimenting with depositing and withdrawing various amounts of cookies. Are you unable to withdraw past the jar’s size? Are you unable to deposit past the jar’s capacity?</li>
</ul>

<p>No <code class="language-plaintext highlighter-rouge">check50</code> for this one!</p>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit! This is a practice problem.</p>


