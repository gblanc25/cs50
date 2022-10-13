<main class="col-md" style="margin-bottom: 265px; margin-top: 0px;">

<a data-id="" id="learning-goals" style="top: 0px;"></a><h2><a data-id="" href="#learning-goals">Learning Goals</a></h2>
<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Work with live data</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Get practice with CSV files and <code class="language-plaintext highlighter-rouge">csv.DictReader</code></li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Practice using dictionaries, lists and exceptions</li>
</ul>

<a data-id="" id="background" style="top: 0px;"></a><h2><a data-id="" href="#background">Background</a></h2>

<p>A popular way to track COVID cases is using a 7-day average. Some states only record cases once a week, so using a 7-day average is much more accurate than daily numbers. In this program, you will be using a <a href="https://github.com/nytimes/covid-19-data">New York Times repository</a> of live, cumulative COVID data to calculate new daily cases, create a 7-day average, and compare this week’s average to the previous week.</p>

<a data-id="" id="getting-started" style="top: 0px;"></a><h2><a data-id="" href="#getting-started">Getting Started</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>Execute <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/6/seven-day-average.zip</code> followed by Enter in order to download a zip called <code class="language-plaintext highlighter-rouge">seven-day-average.zip</code> in your codespace. Take care not to overlook the space between <code class="language-plaintext highlighter-rouge">wget</code> and the following URL, or any other character for that matter!</li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">unzip seven-day-average.zip</code> to create a folder called <code class="language-plaintext highlighter-rouge">seven-day-average</code>.</li>
  <li>You no longer need the ZIP file, so you can execute <code class="language-plaintext highlighter-rouge">rm seven-day-average.zip</code> and respond with “y” followed by Enter at the prompt.</li>
  <li>Finally, right-click or control-click on the <code class="language-plaintext highlighter-rouge">seven-day-average</code> folder and click “Open in CS50 Lab”. You should see the specification for this problem on the left-hand side and its distribution code on the right-hand side.</li>
</ol>

<a data-id="" id="implementation-details" style="top: 0px;"></a><h2><a data-id="" href="#implementation-details">Implementation Details</a></h2>

<p>The distribution code for this problem uses the python <code class="language-plaintext highlighter-rouge">requests</code> library to access the New York Times data stored in an accessible GitHub repository. This is stored as a CSV file. The program then uses <code class="language-plaintext highlighter-rouge">DictReader</code> to read the CSV file. It then creates a <code class="language-plaintext highlighter-rouge">states</code> list to use selected states for calculations.</p>

<p>You will be completing two functions, <code class="language-plaintext highlighter-rouge">calculate</code> and <code class="language-plaintext highlighter-rouge">comparative_averages</code>.</p>

<a data-id="" id="calculate" style="top: 0px;"></a><h3><a data-id="" href="#calculate"><code class="language-plaintext highlighter-rouge">calculate</code></a></h3>

<p>In <code class="language-plaintext highlighter-rouge">calculate</code>, you’ll be creating a dictionary, <code class="language-plaintext highlighter-rouge">new_cases</code>, which will keep track of 14 days of new COVID cases for each state. Keys in this <code class="language-plaintext highlighter-rouge">dict</code> will be the names of states, and the values for each of those keys will be the most recent 14 days of new cases. Since the data from the New York Times is cumulative, each day’s new cases must be calculated by subtracting the previous day’s cases. To do this, you may want to create a second dictionary, <code class="language-plaintext highlighter-rouge">previous_cases</code>, that keeps track of each day’s new cases as it’s calculated.</p>

<ul class="fa-ul">
  <li data-marker="+"><span class="fa-li"><i class="far fa-plus-square"></i></span><span>Hint
    </span><ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>You can store 14 values in the list for each state by appending each new day’s data to end of the list and when the length of the list is great they 14, removing the first element from the list.</li>
    </ul><span>
  </span></li>
</ul>

<p>Your <code class="language-plaintext highlighter-rouge">calculate</code> function should ultimately return the <code class="language-plaintext highlighter-rouge">new_cases</code> dictionary.</p>

<a data-id="" id="comparative_averages" style="top: 0px;"></a><h3><a data-id="" href="#comparative_averages"><code class="language-plaintext highlighter-rouge">comparative_averages</code></a></h3>

<p>Since your <code class="language-plaintext highlighter-rouge">new_cases</code> dictionary is passed to this function, you can calculate this week’s 7-day average by summing up the <em>last</em> 7 elements in the list for a selected state, then dividing this by 7. You can create a 7-day average for the previous week by doing the same with the <em>first</em> 7 elements in that same list.</p>

<ul class="fa-ul">
  <li data-marker="+"><span class="fa-li"><i class="far fa-plus-square"></i></span><span>Hint
    </span><ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Check out python list slicing to easily access a range of elements in a list. For example, <code class="language-plaintext highlighter-rouge">values[3:5]</code> will return the 3rd through 4th indexed elements in the list <code class="language-plaintext highlighter-rouge">values</code>. Note that the second index is <em>not</em> inclusive.</li>
    </ul><span>
  </span></li>
</ul>

<p>You can then calculate the percent increase or decrease, by taking the difference of the two 7-day averages and dividing by last week’s average.</p>

<ul class="fa-ul">
  <li data-marker="+"><span class="fa-li"><i class="far fa-plus-square"></i></span><span>Hint
    </span><ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Note that you can detect division by zero by handling a <code class="language-plaintext highlighter-rouge">ZeroDivisionError</code> with a <code class="language-plaintext highlighter-rouge">try</code> and <code class="language-plaintext highlighter-rouge">except</code> block. For example:</li>
    </ul><span>

    try:
      numerator / denominator
    except ZeroDivisionError:
      ...

    Take a look at Week 3 in "https://cs50.harvard.edu/python/2022/weeks/3/" for more on exceptions in Python.
</ul>

<a data-id="" id="thought-question" style="top: 0px;"></a><h2><a data-id="" href="#thought-question">Thought Question</a></h2>

<p>Why do you think some websites, such as <a href="https://www.washingtonpost.com/graphics/2020/national/coronavirus-us-cases-deaths/?state=US">The Washington Post</a> post different values than your program generates for “Average daily new cases” and “Change in avg. daily cases in last 7 days” for some states, and the same values for others?</p>

<a data-id="" id="how-to-test-your-code" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test-your-code">How to Test Your Code</a></h2>

<p>Your program should behave per the examples below.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>seven-day-average/ $ python seven-day-average.py
Choose one or more states to view average COVID cases.
Press enter when done.

State: Massachusetts
State: New York
State: 

Seven-Day Averages
Massachusetts had a 7-day average of 1646 and an increase of 46%.
New York had a 7-day average of 7502 and a decrease of 1%.
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>seven-day-average/ $ python seven-day-average.py
Choose one or more states to view average COVID cases.
Press enter when done.

State: Maine
State: California
State: 

Seven-Day Averages
California had a 7-day average of 20461 and a decrease of 8%.
Maine had a 7-day average of 196 and a decrease of 10%.
</code></pre></div></div>

<p>Do note that the numbers will vary each day, since the data you are using is updated daily.</p>

<p>No <code class="language-plaintext highlighter-rouge">check50</code> for this one!</p>

<p>To evaluate that the style of your code, type in the following at the <code class="language-plaintext highlighter-rouge">$</code> prompt.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>style50 seven-day-average.py
</code></pre></div></div>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit! This is a practice problem.</p>


