<main class="col-md" style="margin-bottom: 265px; margin-top: 0px;">

<a data-id="" id="learning-goals" style="top: 0px;"></a><h2><a data-id="" href="#learning-goals">Learning Goals</a></h2>
<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Practice working with files and file pointers</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>More work with strings and arrays</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Debugging with <code class="language-plaintext highlighter-rouge">debug50</code></li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Use <code class="language-plaintext highlighter-rouge">valgrind</code> to check for memory leaks</li>
</ul>

<a data-id="" id="background" style="top: 0px;"></a><h2><a data-id="" href="#background">Background</a></h2>

<p>Suppose you work for a company that develops AI-enhanced license plate recognition technology. As you develop your technology, you may want to use actual license plate numbers as test data. You have a text file with some plate numbers you want to analyze, so you first try reading from that text file and printing out the license plates, to test your file-reading logic. But when you run your program, only the last number prints 8 times! What went wrong?</p>

<a data-id="" id="getting-started" style="top: 0px;"></a><h2><a data-id="" href="#getting-started">Getting Started</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>Execute <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/4/license.zip</code> followed by Enter in order to download a zip called <code class="language-plaintext highlighter-rouge">license.zip</code> in your codespace. Take care not to overlook the space between <code class="language-plaintext highlighter-rouge">wget</code> and the following URL, or any other character for that matter!</li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">unzip license.zip</code> to create a folder called <code class="language-plaintext highlighter-rouge">license</code>.</li>
  <li>You no longer need the ZIP file, so you can execute <code class="language-plaintext highlighter-rouge">rm license.zip</code> and respond with “y” followed by Enter at the prompt.</li>
  <li>Finally, right-click or control-click on the <code class="language-plaintext highlighter-rouge">license</code> folder and click “Open in CS50 Lab”. You should see the specification for this problem on the left-hand side and its distribution code on the right-hand side.</li>
</ol>

<a data-id="" id="implementation-details" style="top: 0px;"></a><h2><a data-id="" href="#implementation-details">Implementation Details</a></h2>

<p>If you open the <code class="language-plaintext highlighter-rouge">plates.txt</code> file, you’ll notice that there are actually 8 different license plate numbers. There are a few errors in the distribution code that are causing this to happen. Let’s start by walking through the code.</p>

<p>We first check for command-line arguments, since <code class="language-plaintext highlighter-rouge">argv[1]</code> should be the text file that contains the license plates. We then create a character array of length 7, since the plate numbers are 6 <code class="language-plaintext highlighter-rouge">char</code>s long and we need to save space for the NUL terminator. Now we create an array of <code class="language-plaintext highlighter-rouge">char *</code>’s (character pointers, otherwise known as <code class="language-plaintext highlighter-rouge">string</code>s!) to store the 8 plate numbers. We create a file pointer to our external text file, create a variable to hold the index of each array element, and begin reading the file and saving the plate numbers to the array. Finally, to test that we did this correctly, we print out the values in the array.</p>

<p>However, when we compile and execute this code, something is clearly wrong. You’ll need to make the appropriate corrections!</p>

<a data-id="" id="debugging" style="top: 0px;"></a><h3><a data-id="" href="#debugging">Debugging</a></h3>

<p>Take a close look at what values are actually being added to the array. You can experiment with <code class="language-plaintext highlighter-rouge">debug50</code> to find the error in the distribution code.</p>

<ul class="fa-ul">
  <li data-marker="+"><span class="fa-li"><i class="far fa-plus-square"></i></span><span>Hints
    </span><ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>What exactly does the variable <code class="language-plaintext highlighter-rouge">buffer</code> hold that’s being assigned to each element of the <code class="language-plaintext highlighter-rouge">plates</code> array?</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Note that the <code class="language-plaintext highlighter-rouge">plates</code> array as an array of <code class="language-plaintext highlighter-rouge">char *</code>’s or string pointers.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>So when we assign the char array <code class="language-plaintext highlighter-rouge">buffer</code> to a <code class="language-plaintext highlighter-rouge">char *</code>, what actually happens?</li>
    </ul><span>
  </span></li>
</ul>

<p>Is there a better way to copy license plate numbers to the <code class="language-plaintext highlighter-rouge">license</code> array?</p>

<ul class="fa-ul">
  <li data-marker="+"><span class="fa-li"><i class="far fa-plus-square"></i></span><span>More Hints
    </span><ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Would <code class="language-plaintext highlighter-rouge">strcpy</code> come in useful here?</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>If you copy data to a pointer, where will that data go?</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Is <code class="language-plaintext highlighter-rouge">malloc</code> required here?</li>
    </ul><span>
  </span></li>
</ul>

<a data-id="" id="checking-for-memory-leaks" style="top: 0px;"></a><h3><a data-id="" href="#checking-for-memory-leaks">Checking for Memory Leaks</a></h3>

<p>Once your program seems to be working properly, run valgrind to make sure there are no memory leaks.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>valgrind ./license plates.txt
</code></pre></div></div>

<p>You may end up with something like this:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>==24478== HEAP SUMMARY:
==24478==     in use at exit: 528 bytes in 9 blocks
==24478==   total heap usage: 10 allocs, 1 frees, 4,624 bytes allocated
==24478== 
==24478== 56 bytes in 8 blocks are definitely lost in loss record 1 of 2
==24478==    at 0x4848899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==24478==    by 0x109207: main (license.c:30)
==24478== 
==24478== 472 bytes in 1 blocks are still reachable in loss record 2 of 2
==24478==    at 0x4848899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==24478==    by 0x4A086CD: __fopen_internal (iofopen.c:65)
==24478==    by 0x4A086CD: fopen@@GLIBC_2.2.5 (iofopen.c:86)
==24478==    by 0x1091CD: main (license.c:20)
==24478== 
==24478== LEAK SUMMARY:
==24478==    definitely lost: 56 bytes in 8 blocks
==24478==    indirectly lost: 0 bytes in 0 blocks
==24478==      possibly lost: 0 bytes in 0 blocks
==24478==    still reachable: 472 bytes in 1 blocks
==24478==         suppressed: 0 bytes in 0 blocks
==24478== 
==24478== For lists of detected and suppressed errors, rerun with: -s
==24478== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
</code></pre></div></div>

<p>There seem to be two kinds of memory errors here that need to be corrected!</p>

<ul class="fa-ul">
  <li data-marker="+"><span class="fa-li"><i class="far fa-plus-square"></i></span><span>Hint
    </span><ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Your line numbers may be different, but note here that there seems to be a memory problem in <code class="language-plaintext highlighter-rouge">main</code> on line 30 (something to do with <code class="language-plaintext highlighter-rouge">malloc</code>?), and line 20 (a problem related to <code class="language-plaintext highlighter-rouge">fopen</code>?). What might the distribution code be missing?</li>
    </ul><span>
  </span></li>
</ul>

<a data-id="" id="how-to-test-your-code" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test-your-code">How to Test Your Code</a></h2>

<p>Your program should behave per the examples below.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>license/ $ ./license plates.txt
11ZT00
1KAD21
78ZZ01
99ZZ11
72ZZ21
98ZZ31
44ZW41
34ZZ51
</code></pre></div></div>

<p>You can check your code using <code class="language-plaintext highlighter-rouge">check50</code>, a program that CS50 will use to test your code when you submit, by typing in the following at the <code class="language-plaintext highlighter-rouge">$</code> prompt. But be sure to test it yourself as well!</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>check50 cs50/labs/2022/fall/license
</code></pre></div></div>

<p>To evaluate that the style of your code, type in the following at the <code class="language-plaintext highlighter-rouge">$</code> prompt.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>style50 license.c
</code></pre></div></div>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit! This is a practice problem.</p>


                
