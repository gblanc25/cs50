<main class="col-md" style="margin-bottom: 0px; margin-top: 0px;">

                   
<a data-id="" id="learning-goals" style="top: 0px;"></a><h2><a data-id="" href="#learning-goals">Learning Goals</a></h2>
<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Deepen an understanding of strings</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Practice creating recursive functions</li>
</ul>

<a data-id="" id="background" style="top: 0px;"></a><h2><a data-id="" href="#background">Background</a></h2>

<p>Image that you travel back in time to the 1970’s, when the <code class="language-plaintext highlighter-rouge">C</code> programming language was first created. You are hired as a programmer to come up with a way to convert <code class="language-plaintext highlighter-rouge">string</code>s to <code class="language-plaintext highlighter-rouge">int</code>s. (You may recall that you used a function just like this in Week 2, called <code class="language-plaintext highlighter-rouge">atoi</code>). You want to be thorough in your development process and plan to try several approaches before deciding on the most efficient.</p>

<p>In this problem, you will start with a simple implementation of <code class="language-plaintext highlighter-rouge">atoi</code> that handles positive <code class="language-plaintext highlighter-rouge">int</code>s using loops. You want to rework this into an implementation that uses recursion. Recusive functions can be memory intensive and are not always the best solution, but there are some problems in which using recursion can provide a simpler and more elegant solution.</p>

<p>(Scroll to the bottom of this page to see what an implementation of <code class="language-plaintext highlighter-rouge">atoi</code> might actually look like.)</p>

<ul class="fa-ul">
  <li data-marker="+"><span class="fa-li"><i class="far fa-plus-square"></i></span><span>Hints
    </span><ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Start by getting the index of the last <code class="language-plaintext highlighter-rouge">char</code> in the string (the <code class="language-plaintext highlighter-rouge">char</code> before the <code class="language-plaintext highlighter-rouge">\0</code>).</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Convert this <code class="language-plaintext highlighter-rouge">char</code> into its numeric value. Can you subtract some <code class="language-plaintext highlighter-rouge">char</code> to do this?</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Remove the last <code class="language-plaintext highlighter-rouge">char</code> from the string by moving the null terminator one position to the left.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Return this value plus 10 times the integer value of the new shortened string.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Remember you need a base case when creating a recursive function.</li>
    </ul><span>
  </span></li>
</ul>

<a data-id="" id="getting-started" style="top: 0px;"></a><h2><a data-id="" href="#getting-started">Getting Started</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>Execute <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/3/atoi.zip</code> followed by Enter in order to download a zip called <code class="language-plaintext highlighter-rouge">atoi.zip</code> in your codespace. Take care not to overlook the space between <code class="language-plaintext highlighter-rouge">wget</code> and the following URL, or any other character for that matter!</li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">unzip atoi.zip</code> to create a folder called <code class="language-plaintext highlighter-rouge">atoi</code>.</li>
  <li>You no longer need the ZIP file, so you can execute <code class="language-plaintext highlighter-rouge">rm atoi.zip</code> and respond with “y” followed by Enter at the prompt.</li>
  <li>Finally, right-click or control-click on the <code class="language-plaintext highlighter-rouge">atoi</code> folder and click “Open in CS50 Lab”. You should see the specification for this problem on the left-hand side and its distribution code on the right-hand side.</li>
</ol>

<a data-id="" id="implementation-details" style="top: 0px;"></a><h2><a data-id="" href="#implementation-details">Implementation Details</a></h2>

<p>In the recursive version of <code class="language-plaintext highlighter-rouge">convert</code>, start with the last <code class="language-plaintext highlighter-rouge">char</code> and convert it into an integer value. Then shorten the <code class="language-plaintext highlighter-rouge">string</code>, removing the last <code class="language-plaintext highlighter-rouge">char</code>, and then recursively call <code class="language-plaintext highlighter-rouge">convert</code> using the shortened string as input, where the next <code class="language-plaintext highlighter-rouge">char</code> will be processed.</p>

<a data-id="" id="thought-question" style="top: 0px;"></a><h2><a data-id="" href="#thought-question">Thought Question</a></h2>

<p>Why do you need a base case whenever you create a recursive function?</p>

<a data-id="" id="how-to-test-your-code" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test-your-code">How to Test Your Code</a></h2>

<p>Your program should behave per the examples below.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>atoi/ $ ./atoi
Enter a positive integer: 3432
3432
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>atoi/ $ ./atoi
Enter a positive integer: 98765
98765
</code></pre></div></div>

<p>No <code class="language-plaintext highlighter-rouge">check50</code> for this one!</p>

<p>To evaluate that the style of your code, type in the following at the <code class="language-plaintext highlighter-rouge">$</code> prompt.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>style50 atoi
</code></pre></div></div>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit! This is an optional practice problem.</p>

<p>From <a href="https://www.techiedelight.com/implement-atoi-function-c-iterative-recursive/">techiedelight.com/implement-atoi-function-c-iterative-recursive</a>.</p>
