<p>In <a href="https://en.wikipedia.org/wiki/The_Invitations">season 7, episode 24</a> of <a href="https://en.wikipedia.org/wiki/Seinfeld">Seinfeld</a>, <a href="https://en.wikipedia.org/wiki/Cosmo_Kramer">Kramer</a> visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.</p>

<p>In a file called <code class="language-plaintext highlighter-rouge">bank.py</code>, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output <code class="language-plaintext highlighter-rouge">$0</code>. If the greeting starts with an “h” (but not “hello”), output <code class="language-plaintext highlighter-rouge">$20</code>. Otherwise, output <code class="language-plaintext highlighter-rouge">$100</code>. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.</p>

<details open=""><summary>Hints</summary><ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Recall that a <code class="language-plaintext highlighter-rouge">str</code> comes with quite a few methods, per <a href="https://docs.python.org/3/library/stdtypes.html#string-methods">docs.python.org/3/library/stdtypes.html#string-methods</a>.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Be sure to give $0 not only for “hello” but also “hello there”, “hello, Newman”, and the like.</li>
</ul></details>

<a data-id="" id="demo" style="top: 0px;"></a><h2><a data-id="" href="#demo">Demo</a></h2>

"https://asciinema.org/a/Pes7djS4b1GmwpwqNu2vj6LgY/iframe?autoplay=1&amp;loop=1&amp;cols=80&amp;rows=12"

<a data-id="" id="before-you-begin" style="top: 0px;"></a><h2><a data-id="" href="#before-you-begin">Before You Begin</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>Execute <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/6/bank.zip</code> followed by Enter in order to download a zip called <code class="language-plaintext highlighter-rouge">bank.zip</code> in your codespace. Take care not to overlook the space between <code class="language-plaintext highlighter-rouge">wget</code> and the following URL, or any other character for that matter!</li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">unzip bank.zip</code> to create a folder called <code class="language-plaintext highlighter-rouge">bank</code>.</li>
  <li>You no longer need the ZIP file, so you can execute <code class="language-plaintext highlighter-rouge">rm bank.zip</code> and respond with “y” followed by Enter at the prompt.</li>
  <li>Finally, right-click or control-click on the <code class="language-plaintext highlighter-rouge">bank</code> folder and click “Open in CS50 Lab”. You should see the specification for this problem on the left-hand side and its distribution code on the right-hand side.</li>
</ol>

<a data-id="" id="how-to-test" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test">How to Test</a></h2>

<p>Here’s how to test your code manually:</p>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Run your program with <code class="language-plaintext highlighter-rouge">python bank.py</code>. Type <code class="language-plaintext highlighter-rouge">Hello</code> and press Enter. Your program should output:
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$0 
</code></pre></div>    </div>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Run your program with <code class="language-plaintext highlighter-rouge">python bank.py</code>. Type <code class="language-plaintext highlighter-rouge">Hello, Newman</code> and press Enter. Your program should output:
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$0
</code></pre></div>    </div>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Run your program with <code class="language-plaintext highlighter-rouge">python bank.py</code>. Type <code class="language-plaintext highlighter-rouge">How you doing?</code> and press Enter. Your program should output
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$20
</code></pre></div>    </div>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Run your program with <code class="language-plaintext highlighter-rouge">python bank.py</code>. Type <code class="language-plaintext highlighter-rouge">What's happening?</code> and press Enter. Your program should output
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$100
</code></pre></div>    </div>
  </li>
</ul>

<p>You can execute the below to check your code using <code class="language-plaintext highlighter-rouge">check50</code>, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>check50 cs50/problems/2022/python/bank
</code></pre></div></div>

<p>Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that <code class="language-plaintext highlighter-rouge">check50</code> outputs to see the input <code class="language-plaintext highlighter-rouge">check50</code> handed to your program, what output it expected, and what output your program actually gave.</p>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit! This is a practice problem.</p>
