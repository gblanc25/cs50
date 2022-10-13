<main class="col-md" style="margin-bottom: 265px; margin-top: 0px;">

<a data-id="" id="learning-goals" style="top: 0px;"></a><h2><a data-id="" href="#learning-goals">Learning Goals</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Learn more about data structures</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Work with a trie</li>
</ul>

<a data-id="" id="background" style="top: 0px;"></a><h2><a data-id="" href="#background">Background</a></h2>

<p>Imagine you just rescued a dog and you’re deciding on a name. You found a file online with a list of about 150 of the most popular dog names! You are curious as to whether or not the names you are considering are on this list. Since trie’s are great for data lookups, we’ve given you some (almost!) complete code in <code class="language-plaintext highlighter-rouge">trie.c</code>. There is one function, <code class="language-plaintext highlighter-rouge">check</code>, which is not yet implemented. Your job is to complete this function.</p>

<a data-id="" id="getting-started" style="top: 0px;"></a><h2><a data-id="" href="#getting-started">Getting Started</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>Execute <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/5/trie.zip</code> followed by Enter in order to download a zip called <code class="language-plaintext highlighter-rouge">trie.zip</code> in your codespace. Take care not to overlook the space between <code class="language-plaintext highlighter-rouge">wget</code> and the following URL, or any other character for that matter!</li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">unzip trie.zip</code> to create a folder called <code class="language-plaintext highlighter-rouge">trie</code>.</li>
  <li>You no longer need the ZIP file, so you can execute <code class="language-plaintext highlighter-rouge">rm trie.zip</code> and respond with “y” followed by Enter at the prompt.</li>
  <li>Finally, right-click or control-click on the <code class="language-plaintext highlighter-rouge">trie</code> folder and click “Open in CS50 Lab”. You should see the specification for this problem on the left-hand side and its distribution code on the right-hand side.</li>
</ol>

<a data-id="" id="implementation-details" style="top: 0px;"></a><h2><a data-id="" href="#implementation-details">Implementation Details</a></h2>

<p>Notice that the trie itself is implemented through the creative use of several <code class="language-plaintext highlighter-rouge">struct</code>s called <code class="language-plaintext highlighter-rouge">node</code>. Each <code class="language-plaintext highlighter-rouge">node</code> in a trie has an array of (potential) children, with size 26—one potential child for each letter of the alphabet! Adding words to this trie, notice that—for every letter in a word—we create a new <code class="language-plaintext highlighter-rouge">node</code> child whose parent is either the <code class="language-plaintext highlighter-rouge">root</code> node (for the first letter) or the previous letter (if not the first letter). On the very last letter, we set the <code class="language-plaintext highlighter-rouge">is_word</code> attribute of the child <code class="language-plaintext highlighter-rouge">node</code> to <code class="language-plaintext highlighter-rouge">true</code>. Now, checking if a word is in our trie is as easy as following each letter of that word through our trie. If we get to the final letter and see that <code class="language-plaintext highlighter-rouge">is_word</code> is true, well, that name is in our trie!</p>

<ul class="fa-ul">
  <li data-marker="+"><span class="fa-li"><i class="far fa-plus-square"></i></span><span>Hints
    </span><ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>You probably want to start by setting a <code class="language-plaintext highlighter-rouge">node</code> pointer, <code class="language-plaintext highlighter-rouge">cursor</code> to the <code class="language-plaintext highlighter-rouge">root</code> of the trie.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Iterate through every letter in the argument <code class="language-plaintext highlighter-rouge">word</code> and, as you do, determine the array index that corresponds to that letter.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>You can use the index for a letter to check if <code class="language-plaintext highlighter-rouge">children[index]</code> is a <code class="language-plaintext highlighter-rouge">NULL</code> pointer, meaning the word does not exist in the trie.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>If <code class="language-plaintext highlighter-rouge">children[index]</code> is in fact a node, you can reset <code class="language-plaintext highlighter-rouge">cursor</code> to this node and check for the next letter in its <code class="language-plaintext highlighter-rouge">children</code> nodes.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Remember that the lookup should be case-insensitive. For instance, <code class="language-plaintext highlighter-rouge">A</code> and <code class="language-plaintext highlighter-rouge">a</code> should correspond to 0, <code class="language-plaintext highlighter-rouge">B</code> and <code class="language-plaintext highlighter-rouge">b</code> corresponds to 1, etc.</li>
    </ul><span>
  </span></li>
</ul>

<a data-id="" id="thought-question" style="top: 0px;"></a><h2><a data-id="" href="#thought-question">Thought Question</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>When might you want to use a trie as a data structure? When might you <em>not</em>?</li>
</ul>

<a data-id="" id="how-to-test-your-code" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test-your-code">How to Test Your Code</a></h2>

<p>Your program should behave per the examples below.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>trie/ $ ./trie dog_names.txt
Check word: Molly
Found!
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>trie/ $ ./trie dog_names.txt
Check word: Lucy
Found!
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>trie/ $ ./trie dog_names.txt
Check word: Prudence
Not Found.
</code></pre></div></div>

<p>No <code class="language-plaintext highlighter-rouge">check50</code> for this one!</p>

<p>To evaluate that the style of your code, type in the following at the <code class="language-plaintext highlighter-rouge">$</code> prompt.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>style50 trie.c
</code></pre></div></div>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit! This is a practice problem.</p>


