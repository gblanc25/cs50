<main class="col-md" style="margin-bottom: 265px; margin-top: 0px;">

<a data-id="" id="learning-goals" style="top: 0px;"></a><h2><a data-id="" href="#learning-goals">Learning Goals</a></h2>
<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Practice working with <code class="language-plaintext highlighter-rouge">struct</code>s</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Practice applying sorting algorithms</li>
</ul>

<a data-id="" id="background" style="top: 0px;"></a><h2><a data-id="" href="#background">Background</a></h2>

<p>We seem to be breaking records every year for the hottest weather ever recorded. Climate scientists keep track of what are called “new normals” over multiple years so that we can better predict and prepare for conditions in the near future. The official normals are calculated for a uniform 30 year period, and consist of annual/seasonal, monthly, daily, and hourly averages and statistics of temperature, precipitation, and other climatological variables from almost 15,000 U.S. weather stations.</p>

<p>July is the hottest month of the year for most large US cities. Daytime temperatures above 80 degrees Fahrenheit regularly occur nearly everywhere. The exceptions are some cities along the <a href="https://www.ncei.noaa.gov/products/land-based-station/us-climate-normals">Pacific coast</a>.</p>

<p>In this problem, you will sort the average high temperature values for 10 cities, in decending order.</p>

<ul class="fa-ul">
  <li data-marker="+"><span class="fa-li"><i class="far fa-plus-square"></i></span><span>Hints
    </span><ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>When copying one <code class="language-plaintext highlighter-rouge">struct</code> to another, no need to assign individual elements. The entire <code class="language-plaintext highlighter-rouge">struct</code> can be assigned in one statement.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Even though a <code class="language-plaintext highlighter-rouge">void</code> function cannot return any values, a <code class="language-plaintext highlighter-rouge">return</code> statement can be used to terminate the function.</li>
    </ul><span>
  </span></li>
</ul>
<a data-id="" id="getting-started" style="top: 0px;"></a><h2><a data-id="" href="#getting-started">Getting Started</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>Execute <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/3/temps.zip</code> followed by Enter in order to download a zip called <code class="language-plaintext highlighter-rouge">temps.zip</code> in your codespace. Take care not to overlook the space between <code class="language-plaintext highlighter-rouge">wget</code> and the following URL, or any other character for that matter!</li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">unzip temps.zip</code> to create a folder called <code class="language-plaintext highlighter-rouge">temps</code>.</li>
  <li>You no longer need the ZIP file, so you can execute <code class="language-plaintext highlighter-rouge">rm temps.zip</code> and respond with “y” followed by Enter at the prompt.</li>
  <li>Finally, right-click or control-click on the <code class="language-plaintext highlighter-rouge">temps</code> folder and click “Open in CS50 Lab”. You should see the specification for this problem on the left-hand side and its distribution code on the right-hand side.</li>
</ol>

<a data-id="" id="implementation-details" style="top: 0px;"></a><h2><a data-id="" href="#implementation-details">Implementation Details</a></h2>

<p>The <code class="language-plaintext highlighter-rouge">main</code> function initializes the <code class="language-plaintext highlighter-rouge">temps</code> array, calls the <code class="language-plaintext highlighter-rouge">sort_cities</code> function and prints out the array in sorted order. You will use an O(n<sup>2</sup>) sorting algorithm of your choice (possibly bubble sort, selection sort, or insertion sort) to sort the array by temperature, in descending order.</p>

<a data-id="" id="thought-question" style="top: 0px;"></a><h2><a data-id="" href="#thought-question">Thought Question</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Which of the sorting algorithms did you choose and why?</li>
</ul>

<a data-id="" id="how-to-test-your-code" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test-your-code">How to Test Your Code</a></h2>

<p>Your program should behave per the examples below.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>temps/ $ ./temps

Average July Temperatures by City

Phoenix: 107
Las Vegas: 105
Austin: 97
Miami: 97
Denver: 90
Chicago: 85
New York: 85
Boston: 82
Los Angeles: 82
San Francisco: 66
temps/ $ 
</code></pre></div></div>

<p>No <code class="language-plaintext highlighter-rouge">check50</code> for this one!</p>

<p>To evaluate that the style of your code, type in the following at the <code class="language-plaintext highlighter-rouge">$</code> prompt.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>style50 temps.c
</code></pre></div></div>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit! This is an optional practice problem.</p>


                
