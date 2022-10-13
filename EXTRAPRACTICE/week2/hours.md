<main class="col-md" style="margin-bottom: 42px; margin-top: 0px;">

   

<a data-id="" id="learning-goals" style="top: 0px;"></a><h2><a data-id="" href="#learning-goals">Learning Goals</a></h2>
<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Practice using arrays</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Using an array as a parameter to a function</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Adding values in a loop</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Integer division and type casting</li>
</ul>

<a data-id="" id="background" style="top: 0px;"></a><h2><a data-id="" href="#background">Background</a></h2>
<p>Suppose you’re taking CS50 (if you’re reading this you probably are!) and spending time every week on each problem set. You may be wondering how many hours you’ve spent learning computer science, on average or in total! In this program, you’ll complete a function that calculates, based on a user’s input, a total number of hours <em>or</em> an average number of hours across a given number of days.</p>

<ul class="fa-ul">
  <li data-marker="+"><span class="fa-li"><i class="far fa-plus-square"></i></span><span>Hints
    </span><ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>To add up numbers in an array, you might first want to initialize a variable to zero. After, you’ll want to use a loop that adds each value in the array to that variable.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Be sure to pay attention to what happens if you divide two <code class="language-plaintext highlighter-rouge">int</code>s when calculating the average!</li>
    </ul><span>
  </span></li>
</ul>
  
 


<a data-id="" id="getting-started" style="top: 0px;"></a><h2><a data-id="" href="#getting-started">Getting Started</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>At the <code class="language-plaintext highlighter-rouge">$</code> prompt, type <code class="language-plaintext highlighter-rouge">mkdir hours</code></li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">cd hours</code></li>
  <li>Then copy and paste <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/2/hours.c</code> into your terminal to download this lab’s distribution code.</li>
  <li>You are to complete the function, <code class="language-plaintext highlighter-rouge">calc_hours</code>, which calculates both total hours and average hours, depending on the value of <code class="language-plaintext highlighter-rouge">output</code>.</li>
</ol>

<a data-id="" id="implementation-details" style="top: 0px;"></a><h2><a data-id="" href="#implementation-details">Implementation Details</a></h2>

<p>The <code class="language-plaintext highlighter-rouge">main</code> function prompts the user for the number of weeks a user has been taking CS50, then creates an array with as many elements. Notice that, after retrieving some data, the program prompts the user to type in either “T” or “A”—”T” should (but doesn’t yet!) print the total number of hours the user entered, while “A” should (but doesn’t yet!) print the average hours the user entered. Notice that the <code class="language-plaintext highlighter-rouge">do while</code> loop uses <code class="language-plaintext highlighter-rouge">toupper</code> to capitalize the letter that’s input before it is saved in the variable <code class="language-plaintext highlighter-rouge">output</code>. Then, the <code class="language-plaintext highlighter-rouge">printf</code> function calls <code class="language-plaintext highlighter-rouge">calc_hours</code>. Note the syntax involved when passing an array to a function.</p>

<p>To complete <code class="language-plaintext highlighter-rouge">calc_hours</code>, first total up the hours saved in the array into a new variable. Then, depending on the value of <code class="language-plaintext highlighter-rouge">output</code>, return either this sum, or the average number of hours.</p>

<a data-id="" id="thought-question" style="top: 0px;"></a><h2><a data-id="" href="#thought-question">Thought Question</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>What is the advantage of using a function to calculate hours?</li>
</ul>

<a data-id="" id="how-to-test-your-code" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test-your-code">How to Test Your Code</a></h2>

<p>Your program should behave per the examples below.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>hours/ $ ./hours
Number of weeks taking CS50: 3
Week 0 HW Hours: 3
Week 1 HW Hours: 7
Week 2 HW Hours: 10
Enter T for total hours, A for average hours per week: A
6.7 hours
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>hours/ $ ./hours
Number of weeks taking CS50: 2
Week 0 HW Hours: 2
Week 1 HW Hours: 8
Enter T for total hours, A for average hours per week: T
10.0 hours
</code></pre></div></div>

<p>You can check your code using <code class="language-plaintext highlighter-rouge">check50</code>, a program that CS50 will use to test your code when you submit, by typing in the following at the <code class="language-plaintext highlighter-rouge">$</code> prompt. But be sure to test it yourself as well!</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>check50 cs50/labs/2022/fall/hours
</code></pre></div></div>

<p>To evaluate that the style of your code, type in the following at the <code class="language-plaintext highlighter-rouge">$</code> prompt.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>style50 hours.c
</code></pre></div></div>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit! This is an optional practice problem completed with your lab.</p>
