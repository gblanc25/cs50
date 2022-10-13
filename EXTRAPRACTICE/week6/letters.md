<main class="col-md" style="margin-bottom: 265px; margin-top: 0px;">

<p><a href="https://en.wikipedia.org/wiki/FIGlet">FIGlet</a>, named after <a href="http://www.figlet.org/faq.html">Frank, Ian, and Glen’s letters</a>, is a program from the early 1990s for making large letters out of ordinary text, a form of <a href="https://en.wikipedia.org/wiki/ASCII_art">ASCII art</a>:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code> _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   &lt;  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/
</code></pre></div></div>

<p>Among the fonts supported by FIGlet are those at <a href="http://www.figlet.org/examples.html">figlet.org/examples.html</a>.</p>

<p>FIGlet has since been ported to Python as a module called <a href="https://pypi.org/project/pyfiglet/0.7/">pyfiglet</a>.</p>

<p>In a file called <code class="language-plaintext highlighter-rouge">figlet.py</code>, implement a program that:</p>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Expects zero or two command-line arguments:
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Zero if the user would like to output text in a random font.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Two if the user would like to output text in a specific font, in which case the first of the two should be <code class="language-plaintext highlighter-rouge">-f</code> or <code class="language-plaintext highlighter-rouge">--font</code>, and the second of the two should be the name of the font.</li>
    </ul>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Prompts the user for a <code class="language-plaintext highlighter-rouge">str</code> of text.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Outputs that text in the desired font.</li>
</ul>

<p>If the user provides two command-line arguments and the first is not <code class="language-plaintext highlighter-rouge">-f</code> or <code class="language-plaintext highlighter-rouge">--font</code> or the second is not the name of a font, the program should exit via <code class="language-plaintext highlighter-rouge">sys.exit</code> with an error message.</p>

<details><summary>Hints</summary><ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>You can install <code class="language-plaintext highlighter-rouge">pyfiglet</code> with:
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>pip install pyfiglet
</code></pre></div>    </div>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The documentation for pyfiglet isn’t very clear, but you can use the module as follows:
    <div class="language-py highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kn">from</span> <span class="nn">pyfiglet</span> <span class="kn">import</span> <span class="n">Figlet</span>

<span class="n">figlet</span> <span class="o">=</span> <span class="n">Figlet</span><span class="p">()</span>
</code></pre></div>    </div>
    <p>You can then get a <code class="language-plaintext highlighter-rouge">list</code> of available fonts with code like this:</p>
    <div class="language-py highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">figlet</span><span class="p">.</span><span class="n">getFonts</span><span class="p">()</span>
</code></pre></div>    </div>
    <p>You can set the font with code like this, wherein <code class="language-plaintext highlighter-rouge">f</code> is the font’s name as a <code class="language-plaintext highlighter-rouge">str</code>:</p>
    <div class="language-py highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">figlet</span><span class="p">.</span><span class="n">setFont</span><span class="p">(</span><span class="n">font</span><span class="o">=</span><span class="n">f</span><span class="p">)</span>
</code></pre></div>    </div>
    <p>And you can output text in that font with code like this, wherein <code class="language-plaintext highlighter-rouge">s</code> is that text as a <code class="language-plaintext highlighter-rouge">str</code>:</p>
    <div class="language-py highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">print</span><span class="p">(</span><span class="n">figlet</span><span class="p">.</span><span class="n">renderText</span><span class="p">(</span><span class="n">s</span><span class="p">))</span>
</code></pre></div>    </div>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Note that the <code class="language-plaintext highlighter-rouge">random</code> module comes with quite a few functions, per <a href="https://docs.python.org/3/library/random.html">docs.python.org/3/library/random.html</a>.</li>
</ul></details>

<p>This demo’s first output used a random font. Your output may vary.</p>

<a data-id="" id="before-you-begin" style="top: 0px;"></a><h2><a data-id="" href="#before-you-begin">Before You Begin</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>Execute <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/6/figlet.zip</code> followed by Enter in order to download a zip called <code class="language-plaintext highlighter-rouge">figlet.zip</code> in your codespace. Take care not to overlook the space between <code class="language-plaintext highlighter-rouge">wget</code> and the following URL, or any other character for that matter!</li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">unzip figlet.zip</code> to create a folder called <code class="language-plaintext highlighter-rouge">figlet</code>.</li>
  <li>You no longer need the ZIP file, so you can execute <code class="language-plaintext highlighter-rouge">rm figlet.zip</code> and respond with “y” followed by Enter at the prompt.</li>
  <li>Finally, right-click or control-click on the <code class="language-plaintext highlighter-rouge">figlet</code> folder and click “Open in CS50 Lab”. You should see the specification for this problem on the left-hand side and its distribution code on the right-hand side.</li>
</ol>

<a data-id="" id="how-to-test" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test">How to Test</a></h2>

<p>Here’s how to test your code manually:</p>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Run your program with <code class="language-plaintext highlighter-rouge">python figlet.py test</code>. Your program should exit via <code class="language-plaintext highlighter-rouge">sys.exit</code> and print an error message:
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Invalid usage
</code></pre></div>    </div>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Run your program with <code class="language-plaintext highlighter-rouge">python figlet.py -a slant</code>. Your program should exit via <code class="language-plaintext highlighter-rouge">sys.exit</code> and print an error message:
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Invalid usage
</code></pre></div>    </div>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Run your program with <code class="language-plaintext highlighter-rouge">python figlet.py -f invalid_font</code>. Your program should exit via <code class="language-plaintext highlighter-rouge">sys.exit</code> and print an error message:
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Invalid usage
</code></pre></div>    </div>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Run your program with <code class="language-plaintext highlighter-rouge">python figlet.py -f slant</code>. Type <code class="language-plaintext highlighter-rouge">CS50</code>. Your program should print the following:
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>   ___________ __________ 
  / ____/ ___// ____/ __ \
 / /    \__ \/___ \/ / / /
/ /___ ___/ /___/ / /_/ / 
\____//____/_____/\____/  
</code></pre></div>    </div>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Run your program with <code class="language-plaintext highlighter-rouge">python figlet.py -f rectangles</code>. Type <code class="language-plaintext highlighter-rouge">Hello, world</code>. Your program should print the following:
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code> _____     _ _                        _   _ 
|  |  |___| | |___      _ _ _ ___ ___| |_| |
|     | -_| | | . |_   | | | | . |  _| | . |
|__|__|___|_|_|___| |  |_____|___|_| |_|___|
                  |_|                       
</code></pre></div>    </div>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Run your program with <code class="language-plaintext highlighter-rouge">python figlet.py -f alphabet</code>. Type <code class="language-plaintext highlighter-rouge">Moo</code>. Your program should print the following:
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>M   M         
MM MM         
M M M ooo ooo 
M   M o o o o 
M   M ooo ooo                     
</code></pre></div>    </div>
  </li>
</ul>

<p>You can execute the below to check your code using <code class="language-plaintext highlighter-rouge">check50</code>, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>check50 cs50/problems/2022/python/figlet
</code></pre></div></div>

<p>Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that <code class="language-plaintext highlighter-rouge">check50</code> outputs to see the input <code class="language-plaintext highlighter-rouge">check50</code> handed to your program, what output it expected, and what output your program actually gave.</p>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit! This is a practice problem.</p>


