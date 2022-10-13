<main class="col-md" style="margin-bottom: 265px; margin-top: 0px;">

<a data-id="" id="learning-goals" style="top: 0px;"></a><h2><a data-id="" href="#learning-goals">Learning Goals</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Practice using <code class="language-plaintext highlighter-rouge">struct</code>s</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Write a linear search algorithm</li>
</ul>

<a data-id="" id="background" style="top: 0px;"></a><h2><a data-id="" href="#background">Background</a></h2>

<p>Imagine you’re at the beach and want to order a number of items from the snack bar. You have a limited amount of cash on you, and you want to get a total cost for your items before ordering. In <code class="language-plaintext highlighter-rouge">snackbar.c</code> you will complete two functions. First is <code class="language-plaintext highlighter-rouge">add_items</code> which will add at least the first 4 items on the Beach Burger Shack menu. Then you will complete <code class="language-plaintext highlighter-rouge">get_cost</code> which will implement a linear search algorithm to search for each item you choose, and return the correstponding price.</p>

<ul class="fa-ul">
  <li data-marker="+"><span class="fa-li"><i class="far fa-plus-square"></i></span><span>Hints
    </span><ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>You can hard code the menu items and prices in the <code class="language-plaintext highlighter-rouge">add_items</code> function.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>There is a function in <a href="https://manual.cs50.io/#string.h"><code class="language-plaintext highlighter-rouge">strings.h</code></a> that may come in handy here.</li>
    </ul><span>
  </span></li>
</ul>

<a data-id="" id="getting-started" style="top: 0px;"></a><h2><a data-id="" href="#getting-started">Getting Started</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>Execute <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/3/snackbar.zip</code> followed by Enter in order to download a zip called <code class="language-plaintext highlighter-rouge">snackbar.zip</code> in your codespace. Take care not to overlook the space between <code class="language-plaintext highlighter-rouge">wget</code> and the following URL, or any other character for that matter!</li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">unzip snackbar.zip</code> to create a folder called <code class="language-plaintext highlighter-rouge">snackbar</code>.</li>
  <li>You no longer need the ZIP file, so you can execute <code class="language-plaintext highlighter-rouge">rm snackbar.zip</code> and respond with “y” followed by Enter at the prompt.</li>
  <li>Finally, right-click or control-click on the <code class="language-plaintext highlighter-rouge">snackbar</code> folder and click “Open in CS50 Lab”. You should see the specification for this problem on the left-hand side and its distribution code on the right-hand side.</li>
</ol>

<a data-id="" id="implementation-details" style="top: 0px;"></a><h2><a data-id="" href="#implementation-details">Implementation Details</a></h2>

<p>The <code class="language-plaintext highlighter-rouge">main</code> function is already complete. After calling <code class="language-plaintext highlighter-rouge">add_items</code> to initialize the <code class="language-plaintext highlighter-rouge">menu</code> array, it will print out the menu items and their prices, prompting you to keep selecting items until you press enter without typing anything in. You are to complete two functions, <code class="language-plaintext highlighter-rouge">add_items</code>, which adds at least the first four menu items, and <code class="language-plaintext highlighter-rouge">get_cost</code> to return the cost of each item. When you are creating a linear search algorithm in <code class="language-plaintext highlighter-rouge">get_cost</code>, do make sure that it is case insentive.</p>

<a data-id="" id="thought-question" style="top: 0px;"></a><h2><a data-id="" href="#thought-question">Thought Question</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Why is an array of <code class="language-plaintext highlighter-rouge">struct</code>s a better solution here than multiple arrays?</li>
</ul>

<a data-id="" id="how-to-test-your-code" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test-your-code">How to Test Your Code</a></h2>

<p>Your program should behave as follows:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>snackbar/ $ ./snackbar

Welcome to Beach Burger Shack!
Choose from the following menu to order. Press enter when done.

Burger: $9.50
Vegan Burger: $11.00
Hot Dog: $5.00
Cheese Dog: $7.00
Fries: $5.00
Cheese Fries: $6.00
Cold Pressed Juice: $7.00
Cold Brew: $3.00
Water: $2.00
Soda: $2.00

Enter a food item: burger
Enter a food item: fries
Enter a food item: soda
Enter a food item: 

Your total cost is: $16.50
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>snackbar/ $ ./snackbar

Welcome to Beach Burger Shack!
Choose from the following menu to order. Press enter when done.

Burger: $9.50
Vegan Burger: $11.00
Hot Dog: $5.00
Cheese Dog: $7.00
Fries: $5.00
Cheese Fries: $6.00
Cold Pressed Juice: $7.00
Cold Brew: $3.00
Water: $2.00
Soda: $2.00

Enter a food item: cold brew
Enter a food item: hot dog
Enter a food item: 

Your total cost is: $8.00
</code></pre></div></div>
<p><em>Note that the menu should only print out the items that you saved in the <code class="language-plaintext highlighter-rouge">menu</code> array.</em></p>

<p>No <code class="language-plaintext highlighter-rouge">check50</code> for this one!</p>

<p>To evaluate that the style of your code, type in the following at the <code class="language-plaintext highlighter-rouge">$</code> prompt.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>style50 snackbar.c
</code></pre></div></div>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit! This is an optional practice problem.</p>


              
