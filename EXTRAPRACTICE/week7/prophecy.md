<main class="col-md" style="margin-bottom: 310px; margin-top: 0px;">

<a data-id="" id="learning-goals" style="top: 0px;"></a><h2><a data-id="" href="#learning-goals">Learning Goals</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>“Refactor” a <code class="language-plaintext highlighter-rouge">SQL</code> database to eliminate redundancies</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Use <code class="language-plaintext highlighter-rouge">SELECT</code>, <code class="language-plaintext highlighter-rouge">CREATE</code>, and <code class="language-plaintext highlighter-rouge">INSERT</code> statements to reorganize data</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Write Python to load new <code class="language-plaintext highlighter-rouge">SQL</code> tables</li>
</ul>

<a data-id="" id="background" style="top: 0px;"></a><h2><a data-id="" href="#background">Background</a></h2>

<p>The keeper of the Hall of Prophecy, whose job entailed labelling records and keeping them up to date, decided to create a SQL database of Hogwarts students. Unfortunately the database was poorly designed! The database, <code class="language-plaintext highlighter-rouge">roster.db</code>, contains only one table, <code class="language-plaintext highlighter-rouge">students</code>, with the name and head of each of the four Hogwarts Houses.</p>

<p>Stumbling upon this database, you decide it could be better designed. Take a look at <code class="language-plaintext highlighter-rouge">roster.db</code> and notice how the name and head of each house repeats over and over. A better design would contain a students table (for <em>only</em> students), a houses table (for <em>only</em> houses), and a table that codifies the relationship between students and houses. This process of changing the “schema” of a database is known as <a href="https://en.wikipedia.org/wiki/Database_refactoring">refactoring</a>.</p>

<ul class="fa-ul">
  <li data-marker="+"><span class="fa-li"><i class="far fa-plus-square"></i></span><span>Hint
    </span><ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>You can view the data in the Hall of Prophecy’s table by executing <code class="language-plaintext highlighter-rouge">sqlite3 roster.db</code>, followed by <code class="language-plaintext highlighter-rouge">.schema</code> in your <code class="language-plaintext highlighter-rouge">sqlite3</code> prompt. This will output the <code class="language-plaintext highlighter-rouge">CREATE TABLE</code> statement that was used to generate the <code class="language-plaintext highlighter-rouge">students</code> table.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>You can then use <code class="language-plaintext highlighter-rouge">SELECT</code> statements to view the contents of this table.</li>
    </ul><span>
  </span></li>
</ul>

<a data-id="" id="getting-started" style="top: 0px;"></a><h2><a data-id="" href="#getting-started">Getting Started</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>Execute <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/7/prophecy.zip</code> followed by Enter in order to download a zip called <code class="language-plaintext highlighter-rouge">prophecy.zip</code> in your codespace. Take care not to overlook the space between <code class="language-plaintext highlighter-rouge">wget</code> and the following URL, or any other character for that matter!</li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">unzip prophecy.zip</code> to create a folder called <code class="language-plaintext highlighter-rouge">prophecy</code>.</li>
  <li>You no longer need the ZIP file, so you can execute <code class="language-plaintext highlighter-rouge">rm prophecy.zip</code> and respond with “y” followed by Enter at the prompt.</li>
  <li>Finally, right-click or control-click on the <code class="language-plaintext highlighter-rouge">prophecy</code> folder and click “Open in CS50 Lab”. You should see the specification for this problem on the left-hand side and its distribution code on the right-hand side.</li>
</ol>

<a data-id="" id="implementation-details" style="top: 0px;"></a><h2><a data-id="" href="#implementation-details">Implementation Details</a></h2>

<p>You will use the existing data in <code class="language-plaintext highlighter-rouge">roster.db</code> to create a new database, one with a table for students, a table for houses, and a table for house assignments. You can do this with individual <code class="language-plaintext highlighter-rouge">SQL</code> queries, though we recommend ultimately writing your own Python program to automate the process! Notice we’ve given you the data from the <code class="language-plaintext highlighter-rouge">students</code> table of <code class="language-plaintext highlighter-rouge">roster.db</code> in CSV format, <code class="language-plaintext highlighter-rouge">students.csv</code>, for your convenience.</p>

<a data-id="" id="developing-a-schema" style="top: 0px;"></a><h3><a data-id="" href="#developing-a-schema">Developing a Schema</a></h3>

<p>First, let’s develop a new schema for the database. In <code class="language-plaintext highlighter-rouge">schema.sql</code>, document the three <code class="language-plaintext highlighter-rouge">CREATE TABLE</code> commands you’ll need to create your three new tables.</p>

<p>Keep in mind you’ll want each table to represent a single entity: that is, your students table should represent <em>only</em> students, your houses table should represent only <em>houses</em>, and your house assignments table should represent <em>only</em> house assignments. You might find it helpful to first consider the pieces of information you’ll need in each table, and then about which SQLite data type best represents that information. For example, this was the <code class="language-plaintext highlighter-rouge">CREATE TABLE</code> command for <code class="language-plaintext highlighter-rouge">students</code>:</p>

<div class="language-sql highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">CREATE</span> <span class="k">TABLE</span> <span class="n">students</span> <span class="p">(</span>
    <span class="n">id</span> <span class="nb">INTEGER</span><span class="p">,</span>
    <span class="n">student_name</span> <span class="nb">TEXT</span><span class="p">,</span>
    <span class="n">house</span> <span class="nb">TEXT</span><span class="p">,</span>
    <span class="n">head</span> <span class="nb">TEXT</span><span class="p">,</span>
    <span class="k">PRIMARY</span> <span class="k">KEY</span><span class="p">(</span><span class="n">id</span><span class="p">)</span>
<span class="p">);</span>
</code></pre></div></div>

<p>Keep in mind that every table should have a primary key: a column that uniquely identifies every row in the table. Some tables may be best designed with foreign keys: columns that reference the primary keys of another table.</p>

<p>When you’re ready to configure your database with your new schema, run your three new <code class="language-plaintext highlighter-rouge">CREATE TABLE</code> queries. Type <code class="language-plaintext highlighter-rouge">.schema</code> to see your results.</p>

<a data-id="" id="inserting-data" style="top: 0px;"></a><h3><a data-id="" href="#inserting-data">Inserting Data</a></h3>

<p>After you’ve configured your database with your new schema, you can begin inserting data into your new database (using your new schema!). It’s best to write a Python program here, which can save you the trouble of writing many <code class="language-plaintext highlighter-rouge">INSERT</code> queries. Keep in mind that you have <code class="language-plaintext highlighter-rouge">students.csv</code>, which contains the data from the previous database’s <code class="language-plaintext highlighter-rouge">students</code> table.</p>

<a data-id="" id="thought-question" style="top: 0px;"></a><h2><a data-id="" href="#thought-question">Thought Question</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Why do you think it’s considered better design not to repeat information like houses and heads for each student?</li>
</ul>

<a data-id="" id="how-to-test-your-code" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test-your-code">How to Test Your Code</a></h2>

<p>You’ll likely find the following commands helpful for testing your code:</p>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span><code class="language-plaintext highlighter-rouge">.schema</code> to check the schema of your database</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span><code class="language-plaintext highlighter-rouge">SELECT * FROM table;</code> where <code class="language-plaintext highlighter-rouge">table</code> is the name of the table you’d like to see data from</li>
</ul>

<p>No <code class="language-plaintext highlighter-rouge">check50</code> for this one!</p>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit. This is a practice problem!</p>


               
