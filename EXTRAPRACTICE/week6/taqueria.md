<main class="col-md" style="margin-bottom: 265px; margin-top: 0px;">
  
<p>One of the most popular places to eat in <a href="https://en.wikipedia.org/wiki/Harvard_Square">Harvard Square</a> is <a href="https://www.felipesboston.com/">Felipe’s Taqueria</a>, which offers a <a href="https://www.felipesboston.com/menu">menu</a> of entrees, per the <code class="language-plaintext highlighter-rouge">dict</code> below, wherein the value of each key is a price in dollars:</p>

<div class="language-py highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="p">{</span>
    <span class="s">"Baja Taco"</span><span class="p">:</span> <span class="mf">4.00</span><span class="p">,</span>
    <span class="s">"Burrito"</span><span class="p">:</span> <span class="mf">7.50</span><span class="p">,</span>
    <span class="s">"Bowl"</span><span class="p">:</span> <span class="mf">8.50</span><span class="p">,</span>
    <span class="s">"Nachos"</span><span class="p">:</span> <span class="mf">11.00</span><span class="p">,</span>
    <span class="s">"Quesadilla"</span><span class="p">:</span> <span class="mf">8.50</span><span class="p">,</span>
    <span class="s">"Super Burrito"</span><span class="p">:</span> <span class="mf">8.50</span><span class="p">,</span>
    <span class="s">"Super Quesadilla"</span><span class="p">:</span> <span class="mf">9.50</span><span class="p">,</span>
    <span class="s">"Taco"</span><span class="p">:</span> <span class="mf">3.00</span><span class="p">,</span>
    <span class="s">"Tortilla Salad"</span><span class="p">:</span> <span class="mf">8.00</span>
<span class="p">}</span>
</code></pre></div></div>

<p>In a file called <code class="language-plaintext highlighter-rouge">taqueria.py</code>, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign (<code class="language-plaintext highlighter-rouge">$</code>) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be <a href="https://docs.python.org/3/library/stdtypes.html#str.title">titlecased</a>.</p>

<details><summary>Hints</summary><ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Note that you can detect when the user has inputted control-d by catching an <a href="https://docs.python.org/3/library/exceptions.html#EOFError"><code class="language-plaintext highlighter-rouge">EOFError</code></a> with code like:
    <div class="language-py highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">try</span><span class="p">:</span>
    <span class="n">item</span> <span class="o">=</span> <span class="nb">input</span><span class="p">()</span>
<span class="k">except</span> <span class="nb">EOFError</span><span class="p">:</span>
    <span class="p">...</span>
</code></pre></div>    </div>
    <p>You might want to print a new line so that the user’s cursor (and subsequent prompt) doesn’t remain on the same line as your program’s own prompt.</p>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Inputting control-d does not require inputting Enter as well, and so the user’s cursor (and subsequent prompt) might thus remain on the same line as your program’s own prompt. You can move the user’s cursor to a new line by printing <code class="language-plaintext highlighter-rouge">\n</code> yourself!</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Note that a <code class="language-plaintext highlighter-rouge">dict</code> comes with quite a few methods, per <a href="https://docs.python.org/3/library/stdtypes.html#mapping-types-dict">docs.python.org/3/library/stdtypes.html#mapping-types-dict</a>, among them <code class="language-plaintext highlighter-rouge">get</code>, and supports operations like:
    <div class="language-py highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">d</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>
</code></pre></div>    </div>
    <p>and</p>
    <div class="language-py highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">if</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">d</span><span class="p">:</span>
    <span class="p">...</span>
</code></pre></div>    </div>
    <p>wherein <code class="language-plaintext highlighter-rouge">d</code> is a <code class="language-plaintext highlighter-rouge">dict</code> and <code class="language-plaintext highlighter-rouge">key</code> is a <code class="language-plaintext highlighter-rouge">str</code>.</p>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Be sure to avoid or catch any <a href="https://docs.python.org/3/library/exceptions.html#KeyError"><code class="language-plaintext highlighter-rouge">KeyError</code></a>.</li>
</ul></details>

<a data-id="" id="before-you-begin" style="top: 0px;"></a><h2><a data-id="" href="#before-you-begin">Before You Begin</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>Execute <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/6/taqueria.zip</code> followed by Enter in order to download a zip called <code class="language-plaintext highlighter-rouge">taqueria.zip</code> in your codespace. Take care not to overlook the space between <code class="language-plaintext highlighter-rouge">wget</code> and the following URL, or any other character for that matter!</li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">unzip taqueria.zip</code> to create a folder called <code class="language-plaintext highlighter-rouge">taqueria</code>.</li>
  <li>You no longer need the ZIP file, so you can execute <code class="language-plaintext highlighter-rouge">rm taqueria.zip</code> and respond with “y” followed by Enter at the prompt.</li>
  <li>Finally, right-click or control-click on the <code class="language-plaintext highlighter-rouge">taqueria</code> folder and click “Open in CS50 Lab”. You should see the specification for this problem on the left-hand side and its distribution code on the right-hand side.</li>
</ol>

<a data-id="" id="how-to-test" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test">How to Test</a></h2>

<p>Here’s how to test your code manually:</p>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Run your program with <code class="language-plaintext highlighter-rouge">python taqueria.py</code>. Type <code class="language-plaintext highlighter-rouge">Taco</code> and press Enter, then type <code class="language-plaintext highlighter-rouge">Taco</code> again and press Enter. Your program should output:
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Total: $6.00  
</code></pre></div>    </div>
    <p>and continue prompting the user until they input control-d.</p>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Run your program with <code class="language-plaintext highlighter-rouge">python taqueria.py</code>. Type <code class="language-plaintext highlighter-rouge">Baja Taco</code> and press Enter, then type <code class="language-plaintext highlighter-rouge">Tortilla Salad</code> and press enter. Your program should output:
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Total: $12.00
</code></pre></div>    </div>
    <p>and continue prompting the user until they input control-d.</p>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Run your program with <code class="language-plaintext highlighter-rouge">python taqueria.py</code>. Type <code class="language-plaintext highlighter-rouge">Burger</code> and press Enter. Your program should reprompt the user.</li>
</ul>

<p>Be sure to try other foods and vary the casing of your input. Your program should behave as expected, case-insensitively.</p>

<p>You can execute the below to check your code using <code class="language-plaintext highlighter-rouge">check50</code>, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>check50 cs50/problems/2022/python/taqueria
</code></pre></div></div>

<p>Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that <code class="language-plaintext highlighter-rouge">check50</code> outputs to see the input <code class="language-plaintext highlighter-rouge">check50</code> handed to your program, what output it expected, and what output your program actually gave.</p>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit! This is a practice problem.</p>


