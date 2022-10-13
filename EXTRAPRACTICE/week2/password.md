<main class="col-md" style="margin-bottom: 241px; margin-top: 0px;">

                  

<a data-id="" id="learning-goals" style="top: 0px;"></a><h2><a data-id="" href="#learning-goals">Learning Goals</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Practice iterating through a string</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Practice using the <code class="language-plaintext highlighter-rouge">ctype</code> library</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Practice using Boolean variables</li>
</ul>

<a data-id="" id="background" style="top: 0px;"></a><h2><a data-id="" href="#background">Background</a></h2>

<p>As we all know by now, it’s important to use passwords that are not easy to guess! Many web apps now requre passwords that requre not only alphabetical characters, but also number and symbols.</p>

<p>In this lab, the user is prompted for a password, which will then be validated using a function <code class="language-plaintext highlighter-rouge">check</code> that you will complete. If the password contains at least one upper case letter, one lower case letter, a number and a symbol (meaning a printable character that’s not a letter or number, such as ‘!’, ‘$’ and ‘#’ the function should return <code class="language-plaintext highlighter-rouge">true</code>. If not it should return <code class="language-plaintext highlighter-rouge">false</code>.</p>

<ul class="fa-ul">
  <li data-marker="+"><span class="fa-li"><i class="far fa-plus-square"></i></span><span>Hints
    </span><ol>
      <li>The <code class="language-plaintext highlighter-rouge">ctype</code> library has many useful functions that can come in handy here.</li>
      <li>Boolean variables can keep track of whether each criteria in an algorithm is valid.</li>
    </ol><span>
  </span></li>
</ul>

<a data-id="" id="demo" style="top: 0px;"></a><h2><a data-id="" href="#demo">Demo</a></h2>

![image](https://user-images.githubusercontent.com/90121815/195692476-61fb3b56-7f6c-41bc-b746-a79fea82c767.png)

<a data-id="" id="getting-started" style="top: 0px;"></a><h2><a data-id="" href="#getting-started">Getting Started</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>At the <code class="language-plaintext highlighter-rouge">$</code> prompt, type <code class="language-plaintext highlighter-rouge">mkdir password</code></li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">cd password</code></li>
  <li>Then copy and paste <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/2/password.c</code> into your terminal to download this lab’s distribution code.</li>
  <li>You are to complete the function, <code class="language-plaintext highlighter-rouge">check</code>, which returns <code class="language-plaintext highlighter-rouge">true</code> if the password passes all criteria, and <code class="language-plaintext highlighter-rouge">false</code> if it does not.</li>
</ol>

<a data-id="" id="implementation-details" style="top: 0px;"></a><h2><a data-id="" href="#implementation-details">Implementation Details</a></h2>

<p>Your function will iterate through the password that’s supplied to it as an argument. Since you have to find at least one lower case letter, one upper case letter, one number and one symbol, you may want to create a boolean variable for each and set each to <code class="language-plaintext highlighter-rouge">false</code> before you iterate through the string. If you then find a number, for instance you can set that boolean to <code class="language-plaintext highlighter-rouge">true</code>. If all booleans are <code class="language-plaintext highlighter-rouge">true</code> at the end of the function, it means all criteria are met, and you would return <code class="language-plaintext highlighter-rouge">true</code>.</p>

<a data-id="" id="thought-question" style="top: 0px;"></a><h2><a data-id="" href="#thought-question">Thought Question</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>How many different passwords do you think can be made that are 8 letters long, can use any of 95 printable ASCII characters?</li>
</ul>

<a data-id="" id="how-to-test-your-code" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test-your-code">How to Test Your Code</a></h2>

<p>Your program should behave per the examples below.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>password/ $ ./password
Enter your password: hello
Your password needs at least one uppercase letter, lowercase letter, number and symbol!
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>password/ $ ./password
Enter your password: h3ll(
Your password needs at least one uppercase letter, lowercase letter, number and symbol!
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>password/ $ ./password
Enter your password: h3LL0!
Your password is valid!
</code></pre></div></div>

<p>You can check your code using <code class="language-plaintext highlighter-rouge">check50</code>, a program that CS50 will use to test your code when you submit, by typing in the following at the $ prompt. But be sure to test it yourself as well!</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>check50 cs50/labs/2022/fall/password
</code></pre></div></div>

<p>To evaluate that the style of your code, type in the following at the <code class="language-plaintext highlighter-rouge">$</code> prompt.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>style50 password.c
</code></pre></div></div>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit! This is an optional practice problem completed with your lab.</p>


      
