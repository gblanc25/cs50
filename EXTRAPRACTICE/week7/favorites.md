<main class="col-md" style="margin-bottom: 310px; margin-top: 0px;">

<a data-id="" id="learning-goals" style="top: 0px;"></a><h2><a data-id="" href="#learning-goals">Learning Goals</a></h2>
<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Become familiar with SQL</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Practice using <code class="language-plaintext highlighter-rouge">SELECT</code> and <code class="language-plaintext highlighter-rouge">UPDATE</code> operations</li>
</ul>

<a data-id="" id="background" style="top: 0px;"></a><h2><a data-id="" href="#background">Background</a></h2>

<p>In 2021’s Week 7 lecture, we created a SQL database, <code class="language-plaintext highlighter-rouge">favorites.db</code>, with a table of CS50 students’ favorite TV shows. As often happens when importing raw data, however, we have some inconsistencies and typos to take care of (lest our queries become clumsy and our results inaccurate!).</p>

<p>Your job is to use the SQL <code class="language-plaintext highlighter-rouge">UPDATE</code> keyword to clean up this database, so it can be more effectively used for analysis.</p>

<a data-id="" id="getting-started" style="top: 0px;"></a><h2><a data-id="" href="#getting-started">Getting Started</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>Execute <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/7/favorites.zip</code> followed by Enter in order to download a zip called <code class="language-plaintext highlighter-rouge">favorites.zip</code> in your codespace. Take care not to overlook the space between <code class="language-plaintext highlighter-rouge">wget</code> and the following URL, or any other character for that matter!</li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">unzip favorites.zip</code> to create a folder called <code class="language-plaintext highlighter-rouge">favorites</code>.</li>
  <li>You no longer need the ZIP file, so you can execute <code class="language-plaintext highlighter-rouge">rm favorites.zip</code> and respond with “y” followed by Enter at the prompt.</li>
  <li>Finally, right-click or control-click on the <code class="language-plaintext highlighter-rouge">favorites</code> folder and click “Open in CS50 Lab”. You should see the specification for this problem on the left-hand side and its distribution code on the right-hand side.</li>
</ol>

<a data-id="" id="implementation-details" style="top: 0px;"></a><h2><a data-id="" href="#implementation-details">Implementation Details</a></h2>

<p>Let’s first take a look at the data. Recall that you’ll need to use <a href="https://www.sqlite.org/index.html">SQLite</a>, a lightweight “database engine”, to open <code class="language-plaintext highlighter-rouge">favorites.db</code>. We’ll use the third (and latest) version of SQLite. You can open <code class="language-plaintext highlighter-rouge">favorites.db</code>, then, by executing</p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code>sqlite3 favorites.db
</code></pre></div></div>

<p>so long as your terminal’s working directory is the same directory in which <code class="language-plaintext highlighter-rouge">favorites.db</code> is located.</p>

<p>In your <code class="language-plaintext highlighter-rouge">sqlite3</code> prompt, try executing</p>

<div class="language-sql highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="p">.</span><span class="k">schema</span>
</code></pre></div></div>

<p>to see the commands used to create the two tables in this database, <code class="language-plaintext highlighter-rouge">shows</code> and <code class="language-plaintext highlighter-rouge">genres</code>.</p>

<p>Now try viewing the data inside of <code class="language-plaintext highlighter-rouge">shows</code> by executing</p>

<div class="language-sql highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">SELECT</span> <span class="o">*</span> <span class="k">FROM</span> <span class="n">shows</span><span class="p">;</span>
</code></pre></div></div>

<p>Scrolling up, notice that the very first title in <code class="language-plaintext highlighter-rouge">shows</code> already looks like it might pose a problem. We want “How i met your mother” to be title-cased! Let’s <code class="language-plaintext highlighter-rouge">UPDATE</code> this title by executing</p>

<div class="language-sql highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">UPDATE</span> <span class="n">shows</span> <span class="k">SET</span> <span class="n">title</span> <span class="o">=</span> <span class="nv">"How I Met Your Mother"</span> <span class="k">WHERE</span> <span class="n">title</span> <span class="o">=</span> <span class="nv">"How i met your mother"</span><span class="p">;</span>
</code></pre></div></div>

<p>While you <em>could</em> retype each incorrectly entered show title, it’s much more efficient to select muliple variations of the same show and <code class="language-plaintext highlighter-rouge">UPDATE</code> these to the correct spelling. Maybe the <code class="language-plaintext highlighter-rouge">LIKE</code> keyword could come in handy! There are many titles to clean up, including all of the below:</p>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Adventure Time</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Arrow</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Avatar: The Last Airbender</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Brooklyn Nine-Nine</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Community</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Family Guy</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Friends</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Game of Thrones</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Gilmore Girls</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Grey’s Anatomy</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>How I Met Your Mother</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>It’s Always Sunny in Philadelphia</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Parks and Recreation</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Sherlock</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Squid Game</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The Bachelorette</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The Crown</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The Office</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The Queen’s Gambit</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The Untamed</li>
</ul>

<p>If pressed for time, though, some of the more interesting clean-ups involve these shows:</p>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Brooklyn Nine-Nine</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Game of Thrones</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Grey’s Anatomy</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>It’s Always Sunny in Philadelphia</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Parks and Recreation</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The Office</li>
</ul>

<p>Be sure to save each of these SQL statements to store in a new file <code class="language-plaintext highlighter-rouge">favorites.sql</code>.</p>

<a data-id="" id="thought-question" style="top: 0px;"></a><h2><a data-id="" href="#thought-question">Thought Question</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Why do you think it’s necessary to “clean” data when you can use the SQL <code class="language-plaintext highlighter-rouge">LIKE</code> statement?</li>
</ul>

<a data-id="" id="how-to-test-your-code" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test-your-code">How to Test Your Code</a></h2>

<p>Once you have completed all of your database <code class="language-plaintext highlighter-rouge">UPDATE</code>s, you may want to <code class="language-plaintext highlighter-rouge">SELECT</code> all titles and list these alphabetically to make sure that all are correct.</p>

<p>No <code class="language-plaintext highlighter-rouge">check50</code> for this one!</p>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit. This is a practice problem!</p>
