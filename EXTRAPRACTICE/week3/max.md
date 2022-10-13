<main class="col-md" style="margin-bottom: 265px; margin-top: 0px;">

<a data-id="" id="learning-goals" style="top: 0px;"></a><h2><a data-id="" href="#learning-goals">Learning Goals</a></h2>
<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Pass an array into a function</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Create a helper function that finds a maximum value</li>
</ul>

<a data-id="" id="background" style="top: 0px;"></a><h2><a data-id="" href="#background">Background</a></h2>
<p>There are many situations where you’ll find it helpful to have a function that finds the maximum (and minimum) value in an array. Since there is no built-in <code class="language-plaintext highlighter-rouge">max</code> function in <code class="language-plaintext highlighter-rouge">C</code>, you’ll create one in this practice problem. You can then use it in upcoming problem sets where it may be helpful!</p>

<ul class="fa-ul">
  <li data-marker="+"><span class="fa-li"><i class="far fa-plus-square"></i></span><span>Hints
    </span><ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Start out with a variable that keeps track of your max value. There are two ways to initialize this. You can start out using the lowest possible value (be careful you don’t start with zero, as the max value could be a negative number!) or you can start with the first element in the array.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Loop through the array and reset this max value every time you find a value that’s larger.</li>
    </ul><span>
  </span></li>
</ul>

<a data-id="" id="getting-started" style="top: 0px;"></a><h2><a data-id="" href="#getting-started">Getting Started</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>Execute <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/3/max.zip</code> followed by Enter in order to download a zip called <code class="language-plaintext highlighter-rouge">max.zip</code> in your codespace. Take care not to overlook the space between <code class="language-plaintext highlighter-rouge">wget</code> and the following URL, or any other character for that matter!</li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">unzip max.zip</code> to create a folder called <code class="language-plaintext highlighter-rouge">max</code>.</li>
  <li>You no longer need the ZIP file, so you can execute <code class="language-plaintext highlighter-rouge">rm max.zip</code> and respond with “y” followed by Enter at the prompt.</li>
  <li>Finally, right-click or control-click on the <code class="language-plaintext highlighter-rouge">max</code> folder and click “Open in CS50 Lab”. You should see the specification for this problem on the left-hand side and its distribution code on the right-hand side.</li>
</ol>

<a data-id="" id="implementation-details" style="top: 0px;"></a><h2><a data-id="" href="#implementation-details">Implementation Details</a></h2>

<p>The <code class="language-plaintext highlighter-rouge">main</code> function initializes the array, asks the user to enter values, and then passes the array and the number of items to the <code class="language-plaintext highlighter-rouge">max</code> function. Complete the <code class="language-plaintext highlighter-rouge">max</code> function by iterating through even element in the array, and return the maximum value.</p>

<a data-id="" id="thought-question" style="top: 0px;"></a><h2><a data-id="" href="#thought-question">Thought Question</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>What types of programs can you think of that might benefit from a <code class="language-plaintext highlighter-rouge">max</code> helper function?</li>
</ul>

<a data-id="" id="how-to-test-your-code" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test-your-code">How to Test Your Code</a></h2>

<p>Your program should behave per the examples below.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>max/ $ ./max
Number of elements: 3
Element 0: 2
Element 1: 10
Element 2: -1
The max value is 10.
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>max/ $ ./max
Number of elements: 4
Element 0: -100
Element 1: -200
Element 2: -3
Element 3: -5000
The max value is -3.
</code></pre></div></div>

<p>You can check your code using <code class="language-plaintext highlighter-rouge">check50</code>, a program that CS50 will use to test your code when you submit, by typing in the following at the <code class="language-plaintext highlighter-rouge">$</code> prompt. But be sure to test it yourself as well!</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>check50 cs50/labs/2022/fall/max
</code></pre></div></div>

<p>To evaluate that the style of your code, type in the following at the <code class="language-plaintext highlighter-rouge">$</code> prompt.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>style50 max.c
</code></pre></div></div>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit! This is an optional practice problem.</p>


               
