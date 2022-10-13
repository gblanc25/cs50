<main class="col-md" style="margin-bottom: 265px; margin-top: 0px;">

<a data-id="" id="learning-goals" style="top: 0px;"></a><h2><a data-id="" href="#learning-goals">Learning Goals</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Practice working with images</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Learn about metadata</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Learn more about how <code class="language-plaintext highlighter-rouge">struct</code>s can be useful</li>
</ul>

<a data-id="" id="background" style="top: 0px;"></a><h2><a data-id="" href="#background">Background</a></h2>

<p>Imagine an image you need to present to your boss for a major presentation somehow got corrupted! Upon investigating, you find that the image is mostly intact. Except, when you view the image, it now appears to be upside down!</p>

<p>Recall that a digital image file is just a sequence of bits, arranged in some fashion. A 24-bit BMP file, then, is essentially just a sequence of bits, (almost) every 24 of which happen to represent some pixel’s color. But a BMP file also contains some “metadata,” information like an image’s height and width. That metadata is stored at the beginning of the file in the form of two data structures generally referred to as “headers,” not to be confused with C’s header files. The first of these headers, called <code class="language-plaintext highlighter-rouge">BITMAPFILEHEADER</code>, is 14 bytes long. (Recall that 1 byte equals 8 bits.) The second of these headers, called <code class="language-plaintext highlighter-rouge">BITMAPINFOHEADER</code>, is 40 bytes long. Immediately following these headers is the actual bitmap: an array of bytes, triples of which represent a pixel’s color.</p>

<p>Your job is to edit the metadata programmatically so that the bitmap’s top row is first and bottom row last. Best to avoid editing the pixels directly, lest you further corrupt the file!</p>

<ul class="fa-ul">
  <li data-marker="+"><span class="fa-li"><i class="far fa-plus-square"></i></span><span>Hints
    </span><ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Be sure to look carefully at the members of the <code class="language-plaintext highlighter-rouge">BITMAPINFOHEADER</code> <code class="language-plaintext highlighter-rouge">struct</code> in <code class="language-plaintext highlighter-rouge">bmp.h</code>.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>If you read the <a href="https://learn.microsoft.com/en-us/previous-versions//dd183376(v=vs.85)">documentation</a> for each of these members, which should you modify? How so?</li>
    </ul><span>
  </span></li>
</ul>

<a data-id="" id="getting-started" style="top: 0px;"></a><h2><a data-id="" href="#getting-started">Getting Started</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>Execute <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/4/bottomup.zip</code> followed by Enter in order to download a zip called <code class="language-plaintext highlighter-rouge">bottomup.zip</code> in your codespace. Take care not to overlook the space between <code class="language-plaintext highlighter-rouge">wget</code> and the following URL, or any other character for that matter!</li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">unzip bottomup.zip</code> to create a folder called <code class="language-plaintext highlighter-rouge">bottomup</code>.</li>
  <li>You no longer need the ZIP file, so you can execute <code class="language-plaintext highlighter-rouge">rm bottomup.zip</code> and respond with “y” followed by Enter at the prompt.</li>
  <li>Finally, right-click or control-click on the <code class="language-plaintext highlighter-rouge">bottomup</code> folder and click “Open in CS50 Lab”. You should see the specification for this problem on the left-hand side and its distribution code on the right-hand side.</li>
</ol>

<a data-id="" id="implementation-details" style="top: 0px;"></a><h2><a data-id="" href="#implementation-details">Implementation Details</a></h2>

<p>Go ahead and pull up the URLs to which <code class="language-plaintext highlighter-rouge">BITMAPFILEHEADER</code> and <code class="language-plaintext highlighter-rouge">BITMAPINFOHEADER</code> are attributed, per the comments in <code class="language-plaintext highlighter-rouge">bmp.h</code>. Take a close look at the members of the <code class="language-plaintext highlighter-rouge">BITMAPINFOHEADER</code> <code class="language-plaintext highlighter-rouge">struct</code>. Use that information to write a bit of code in <code class="language-plaintext highlighter-rouge">bottomup.c</code> to change the image from bottom-up to top-down. The code in question needn’t be very complicated, particularly if you know what you’re doing!</p>

<a data-id="" id="thought-question" style="top: 0px;"></a><h2><a data-id="" href="#thought-question">Thought Question</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Why do image files need metadata?</li>
</ul>

<a data-id="" id="how-to-test-your-code" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test-your-code">How to Test Your Code</a></h2>

<p>Your program should behave per the examples below.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>bottomup/ $ ./bottomup harvard_bottomup.bmp harvard_topdown.bmp
</code></pre></div></div>

<p>When your program is working correctly, you should see a new file, <code class="language-plaintext highlighter-rouge">harvard_topdown.bmp</code> in your <code class="language-plaintext highlighter-rouge">bottomup</code> directory. Open it up and see if the orientation of the image is correct.</p>

<p>You can check your code using <code class="language-plaintext highlighter-rouge">check50</code>, a program that CS50 will use to test your code when you submit, by typing in the following at the <code class="language-plaintext highlighter-rouge">$</code> prompt. But be sure to test it yourself as well!</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>check50 cs50/labs/2022/fall/bottomup
</code></pre></div></div>

<p>To evaluate that the style of your code (indentations and spacing) is correct, type in the following at the <code class="language-plaintext highlighter-rouge">$</code> prompt.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>style50 bottomup.c
</code></pre></div></div>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit! This is a practice problem.</p>


