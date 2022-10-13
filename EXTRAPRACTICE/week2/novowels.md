<main class="col-md" style="margin-bottom: 241px; margin-top: 0px;">

                

<a data-id="" id="learning-goals" style="top: 0px;"></a><h2><a data-id="" href="#learning-goals">Learning Goals</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Practice using strings</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Practice using command-line arguments</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Write a program entirely from scratch</li>
</ul>

<a data-id="" id="background" style="top: 0px;"></a><h2><a data-id="" href="#background">Background</a></h2>

<p>If you’ve been on the internet, you might have seen <a href="https://en.wikipedia.org/wiki/Leet">“leetspeak”</a> (or “l33tsp36k” for our purposes!), which involves the substitution of symbols for alphabetical characters, where those symbols somewhat resemble their alphabetical counterparts. In this lab, you’ll write a program to replace certain vowels with digits!</p>

<p>Up until now, you’ve frequently written programs for which you’ve been provided distribution code. You’ll notice when downloading the “distro” for this problem, you start with nothing more than a couple of commonly used libraries and an empty <code class="language-plaintext highlighter-rouge">main</code> function. In this problem, you will convert a word, which you will input at the command line, to a corresponding word with numbers replacing vowels.</p>

<ul class="fa-ul">
  <li data-marker="+"><span class="fa-li"><i class="far fa-plus-square"></i></span><span>Hints
    </span><ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Do note that the <code class="language-plaintext highlighter-rouge">main</code> function in the distribution code uses <code class="language-plaintext highlighter-rouge">argc</code> and <code class="language-plaintext highlighter-rouge">argv</code>. Be sure to use these!</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Be sure to check for the correct number of command-line arguments before doing anything else in your <code class="language-plaintext highlighter-rouge">main</code> function.</li>
    </ul><span>
  </span></li>
</ul>

<a data-id="" id="demo" style="top: 0px;"></a><h2><a data-id="" href="#demo">Demo</a></h2>

![image](https://user-images.githubusercontent.com/90121815/195692221-e24d3070-5556-4d27-9593-b075e9ed8ac5.png)

<a data-id="" id="getting-started" style="top: 0px;"></a><h2><a data-id="" href="#getting-started">Getting Started</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>At the <code class="language-plaintext highlighter-rouge">$</code> prompt, type <code class="language-plaintext highlighter-rouge">mkdir no-vowels</code></li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">cd no-vowels</code></li>
  <li>Then copy and paste <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/2/no-vowels.c</code> into your terminal to download this lab’s distribution code.</li>
</ol>

<a data-id="" id="implementation-details" style="top: 0px;"></a><h2><a data-id="" href="#implementation-details">Implementation Details</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Implement your program in a file called <code class="language-plaintext highlighter-rouge">no-vowels.c</code> in a directory called <code class="language-plaintext highlighter-rouge">no-vowels</code>.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Your program must accept a single command-line argument, which will be the word that you want to convert.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>If your program is executed without any command-line arguments or with more than one command-line argument, your program should print an error message of your choice (with <code class="language-plaintext highlighter-rouge">printf</code>) and <code class="language-plaintext highlighter-rouge">return</code> from <code class="language-plaintext highlighter-rouge">main</code> a value of 1 (which tends to signify an error) immediately.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Your program must contain a function called <code class="language-plaintext highlighter-rouge">replace</code> which takes a <code class="language-plaintext highlighter-rouge">string</code> input and returns a <code class="language-plaintext highlighter-rouge">string</code> output.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>This function will change the following vowels to numbers: <code class="language-plaintext highlighter-rouge">a</code> becomes <code class="language-plaintext highlighter-rouge">6</code>, <code class="language-plaintext highlighter-rouge">e</code> becomes <code class="language-plaintext highlighter-rouge">3</code>, <code class="language-plaintext highlighter-rouge">i</code> becomes <code class="language-plaintext highlighter-rouge">1</code>, <code class="language-plaintext highlighter-rouge">o</code> becomes <code class="language-plaintext highlighter-rouge">0</code> and <code class="language-plaintext highlighter-rouge">u</code> does not change.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The input parameter for the <code class="language-plaintext highlighter-rouge">replace</code> function will be <code class="language-plaintext highlighter-rouge">argv[1]</code> and the return value is the converted word.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The main function will then print the converted word, followed by <code class="language-plaintext highlighter-rouge">\n</code>.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>You may want to try using the <a href="https://cs50.readthedocs.io/style/c/#switches"><code class="language-plaintext highlighter-rouge">switch</code> statement</a> in your <code class="language-plaintext highlighter-rouge">replace</code> function.</li>
</ul>

<a data-id="" id="thought-question" style="top: 0px;"></a><h2><a data-id="" href="#thought-question">Thought Question</a></h2>

<p>Why might you want to use command-line arguments rather than <code class="language-plaintext highlighter-rouge">get_string</code>, <code class="language-plaintext highlighter-rouge">get_int</code>, etc?</p>

<a data-id="" id="how-to-test-your-code" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test-your-code">How to Test Your Code</a></h2>

<p>Your program should behave per the examples below.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>no-vowels/ $ ./no-vowels
Usage: ./no-vowels word
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>no-vowels/ $ ./no-vowels hello
h3ll0
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>no-vowels/ $ ./no-vowels pseudocode
ps3ud0c0d3
</code></pre></div></div>

<p>You can check your code using <code class="language-plaintext highlighter-rouge">check50</code>, a program that CS50 will use to test your code when you submit, by typing in the following at the <code class="language-plaintext highlighter-rouge">$</code> prompt. But be sure to test it yourself as well!</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>check50 cs50/labs/2022/fall/no-vowels
</code></pre></div></div>
<p>Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that <code class="language-plaintext highlighter-rouge">check50</code> outputs to see the input <code class="language-plaintext highlighter-rouge">check50</code> handed to your program, what output it expected, and what output your program actually gave.</p>

<p>To evaluate that the style of your code (indentations and spacing) is correct, type in the following at the <code class="language-plaintext highlighter-rouge">$</code> prompt.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>style50 no-vowels.c
</code></pre></div></div>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit! This is an optional practice problem completed with your lab.</p>
