<main class="col-md" style="margin-bottom: 272px; margin-top: 0px;">

<a data-id="" id="learning-goals" style="top: 0px;"></a><h2><a data-id="" href="#learning-goals">Learning Goals</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Become aquainted with the history of web design</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Learn to use modern web development tools</li>
</ul>

<a data-id="" id="background" style="top: 0px;"></a><h2><a data-id="" href="#background">Background</a></h2>

<p>The world wide web as we know it has only been around since the mid 1990’s. Early tools to develop websites were very limited: there was no CSS or JavaScript and HTML was rendered differently on different browsers. One of the earliest sites was <a href="https://amazon.com">amazon.com</a>.</p>

![image](https://user-images.githubusercontent.com/90121815/198883712-bdf6a23a-cc2b-4b63-a817-62cce3e9951a.png)

<p>Quite a different look than today!</p>

<p>Another early site was RadioShack. Their first website in 1996 had a look very similar to websites of that time. The hottest design elements were clunky-looking buttons and repeating background patterns.</p>

![image](https://user-images.githubusercontent.com/90121815/198883725-0afed63c-d1e9-467f-9270-3f18a9948409.png)

<p>A common feature on early sites was a link to a “text only” version of the web page. Because internet connections were so slow, images could be very slow to load! The oversized RadioShack logo and its corresponding buttons are actually one image here: the buttons are activated using an html <code class="language-plaintext highlighter-rouge">map</code> feature, which is still available today, but rarely used.</p>

<div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nt">&lt;map</span> <span class="na">name=</span><span class="s">"rsmap"</span><span class="nt">&gt;</span>
<span class="nt">&lt;area</span> <span class="na">shape=</span><span class="s">"rect"</span> <span class="na">coords=</span><span class="s">"8,246,122,297"</span> <span class="na">href=</span><span class="s">"http://www.radioshack.com/rsstorelocator/rszip?1"</span><span class="nt">&gt;</span>
<span class="nt">&lt;area</span> <span class="na">shape=</span><span class="s">"rect"</span> <span class="na">coords=</span><span class="s">"123,246,240,297"</span> <span class="na">href=</span><span class="s">"http://www.radioshack.com/rsfuture.html"</span><span class="nt">&gt;</span>
<span class="nt">&lt;area</span> <span class="na">shape=</span><span class="s">"rect"</span> <span class="na">coords=</span><span class="s">"241,246,358,297"</span> <span class="na">href=</span><span class="s">"http://www.tandy.com/contacts/"</span><span class="nt">&gt;</span>
<span class="nt">&lt;area</span> <span class="na">shape=</span><span class="s">"rect"</span> <span class="na">coords=</span><span class="s">"359,246,475,297"</span> <span class="na">href=</span><span class="s">"http://www.tandy.com/press.html"</span><span class="nt">&gt;</span>
<span class="nt">&lt;area</span> <span class="na">shape=</span><span class="s">"rect"</span> <span class="na">coords=</span><span class="s">"476,246,599,297"</span> <span class="na">href=</span><span class="s">"http://www.radioshack.com/history/"</span><span class="nt">&gt;</span>
<span class="nt">&lt;/map&gt;</span>
</code></pre></div></div>

<p>There was very little control over typography and the only fonts available were those that resided on a visitor’s computer. So a web designer had to be careful to use only very common, standard fonts.</p>

<p>By 1997, RadioShack significantly upgraded the look of their site, and it now looked like this. Note the 3-D spinning “R”, another popular feature on websites of that time!</p>

![image](https://user-images.githubusercontent.com/90121815/198883758-2fc468f7-2d1a-4e98-a674-0bd72e8b96e3.png)

<p>To create a layout like this with columns and rows, the entire page is constructed from an HTML table, with a 1-by-1 pixel image, <code class="language-plaintext highlighter-rouge">dot_clear.gif</code>, to control the visual layout of HTML elements on a web page, since the HTML standard at the time did not allow this. Tables were not created for this purpose, but designers had few options for controling the layout of the page.</p>

<div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nt">&lt;table</span> <span class="na">border=</span><span class="s">"0"</span> <span class="na">cellspacing=</span><span class="s">"0"</span> <span class="na">cellpadding=</span><span class="s">"0"</span> <span class="na">width=</span><span class="s">"969"</span><span class="nt">&gt;&lt;tr</span> <span class="na">valign=</span><span class="s">"top"</span> <span class="na">align=</span><span class="s">"left"</span><span class="nt">&gt;</span>
	<span class="nt">&lt;td</span> <span class="na">colspan=</span><span class="s">"1"</span> <span class="na">width=</span><span class="s">"10"</span><span class="nt">&gt;&lt;img</span> <span class="na">src=</span><span class="s">"dot_clear.gif"</span> <span class="na">width=</span><span class="s">"10"</span> <span class="na">height=</span><span class="s">"1"</span> <span class="na">border=</span><span class="s">"0"</span><span class="nt">&gt;&lt;/td&gt;</span>
	<span class="nt">&lt;td</span> <span class="na">colspan=</span><span class="s">"1"</span> <span class="na">width=</span><span class="s">"2"</span><span class="nt">&gt;&lt;img</span> <span class="na">src=</span><span class="s">"dot_clear.gif"</span> <span class="na">width=</span><span class="s">"2"</span> <span class="na">height=</span><span class="s">"1"</span> <span class="na">border=</span><span class="s">"0"</span><span class="nt">&gt;&lt;/td&gt;</span>
	<span class="nt">&lt;td</span> <span class="na">colspan=</span><span class="s">"1"</span> <span class="na">width=</span><span class="s">"35"</span><span class="nt">&gt;&lt;img</span> <span class="na">src=</span><span class="s">"dot_clear.gif"</span> <span class="na">width=</span><span class="s">"35"</span> <span class="na">height=</span><span class="s">"1"</span> <span class="na">border=</span><span class="s">"0"</span><span class="nt">&gt;&lt;/td</span>
 <span class="err">...</span>
</code></pre></div></div>

<p>Since there was still limited choices for fonts, all of the type you see on this page that is not the standard “Times Roman” was created as an image and imported into the web page.</p>

<p><a href="https://www.justinmind.com/blog/10-90s-websites-designs-you-wont-believe-existed/">Take a look at some other website designs from the 90’s.</a></p>

<p>Now you’ll re-design RadioShack’s website (just the homepage is fine!) using modern web development tools. No tables, html maps or spinning logos please!</p>

<a data-id="" id="getting-started" style="top: 0px;"></a><h2><a data-id="" href="#getting-started">Getting Started</a></h2>

<ol>
  <li>Log into <a href="https://code.cs50.io/">code.cs50.io</a> using your GitHub account.</li>
  <li>Click inside the terminal window and execute <code class="language-plaintext highlighter-rouge">cd</code>.</li>
  <li>Execute <code class="language-plaintext highlighter-rouge">wget https://cdn.cs50.net/2022/fall/labs/8/redo.zip</code> followed by Enter in order to download a zip called <code class="language-plaintext highlighter-rouge">redo.zip</code> in your codespace. Take care not to overlook the space between <code class="language-plaintext highlighter-rouge">wget</code> and the following URL, or any other character for that matter!</li>
  <li>Now execute <code class="language-plaintext highlighter-rouge">unzip redo.zip</code> to create a folder called <code class="language-plaintext highlighter-rouge">redo</code>.</li>
  <li>You no longer need the ZIP file, so you can execute <code class="language-plaintext highlighter-rouge">rm redo.zip</code> and respond with “y” followed by Enter at the prompt.</li>
  <li>Finally, right-click or control-click on the <code class="language-plaintext highlighter-rouge">redo</code> folder and click “Open in CS50 Lab”. You should see the specification for this problem on the left-hand side and its distribution code on the right-hand side.</li>
</ol>

<a data-id="" id="implementation-details" style="top: 0px;"></a><h2><a data-id="" href="#implementation-details">Implementation Details</a></h2>

<p>Notice that you’ve received three folders, <code class="language-plaintext highlighter-rouge">radio1996/</code>, <code class="language-plaintext highlighter-rouge">radio1997/</code>, and <code class="language-plaintext highlighter-rouge">radiotoday/</code>. You can explore implementations of Radio Shack’s website from 1996 and 1997, but you’ll ultimately create your own iteration in <code class="language-plaintext highlighter-rouge">radiotoday/</code>.</p>

<p>One of the most popular front-end web development tools in use these days is <a href="https://getbootstrap.com/docs/">Bootstrap</a>. It’s free, open-source, and designed to enable responsive development of websites and web apps. It’s built on top of CSS and JavaScript to allow developers to create websites quickly and without having to recreate commonly used features such as interactive buttons, navigation systems, columns and grids.</p>

<p>Start your redesign by trying out bootstrap’s <a href="https://getbootstrap.com/docs/5.2/components/navbar/">Navbar</a> feature to easily create a custom navigation bar to handle all the menu options. Scoll down on this bootstrap documentation until you see a simple navigation bar with minimal code and copy this code to the top of the <code class="language-plaintext highlighter-rouge">body</code> section of <code class="language-plaintext highlighter-rouge">index.html</code>.</p>

<div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nt">&lt;nav</span> <span class="na">class=</span><span class="s">"navbar navbar-expand-lg bg-light"</span><span class="nt">&gt;</span>
  <span class="nt">&lt;div</span> <span class="na">class=</span><span class="s">"container-fluid"</span><span class="nt">&gt;</span>
    <span class="nt">&lt;a</span> <span class="na">class=</span><span class="s">"navbar-brand"</span> <span class="na">href=</span><span class="s">"#"</span><span class="nt">&gt;</span>Navbar<span class="nt">&lt;/a&gt;</span>
    <span class="nt">&lt;button</span> <span class="na">class=</span><span class="s">"navbar-toggler"</span> <span class="na">type=</span><span class="s">"button"</span> <span class="na">data-bs-toggle=</span><span class="s">"collapse"</span> <span class="na">data-bs-target=</span><span class="s">"#navbarNavAltMarkup"</span> <span class="na">aria-controls=</span><span class="s">"navbarNavAltMarkup"</span> <span class="na">aria-expanded=</span><span class="s">"false"</span> <span class="na">aria-label=</span><span class="s">"Toggle navigation"</span><span class="nt">&gt;</span>
      <span class="nt">&lt;span</span> <span class="na">class=</span><span class="s">"navbar-toggler-icon"</span><span class="nt">&gt;&lt;/span&gt;</span>
    <span class="nt">&lt;/button&gt;</span>
    <span class="nt">&lt;div</span> <span class="na">class=</span><span class="s">"collapse navbar-collapse"</span> <span class="na">id=</span><span class="s">"navbarNavAltMarkup"</span><span class="nt">&gt;</span>
      <span class="nt">&lt;div</span> <span class="na">class=</span><span class="s">"navbar-nav"</span><span class="nt">&gt;</span>
        <span class="nt">&lt;a</span> <span class="na">class=</span><span class="s">"nav-link active"</span> <span class="na">aria-current=</span><span class="s">"page"</span> <span class="na">href=</span><span class="s">"#"</span><span class="nt">&gt;</span>Home<span class="nt">&lt;/a&gt;</span>
        <span class="nt">&lt;a</span> <span class="na">class=</span><span class="s">"nav-link"</span> <span class="na">href=</span><span class="s">"#"</span><span class="nt">&gt;</span>Features<span class="nt">&lt;/a&gt;</span>
        <span class="nt">&lt;a</span> <span class="na">class=</span><span class="s">"nav-link"</span> <span class="na">href=</span><span class="s">"#"</span><span class="nt">&gt;</span>Pricing<span class="nt">&lt;/a&gt;</span>
        <span class="nt">&lt;a</span> <span class="na">class=</span><span class="s">"nav-link disabled"</span><span class="nt">&gt;</span>Disabled<span class="nt">&lt;/a&gt;</span>
      <span class="nt">&lt;/div&gt;</span>
    <span class="nt">&lt;/div&gt;</span>
  <span class="nt">&lt;/div&gt;</span>
<span class="nt">&lt;/nav&gt;</span>
</code></pre></div></div>

<p>When you run <code class="language-plaintext highlighter-rouge">http-server</code> to preview your web page, you’ll see menu items on top such as “Features”, “Pricing”, etc. Change these to represent the appropriate menu items for your RadioShack homepage. You don’t need to create additional pages for these to link to, but if you did, you would change <code class="language-plaintext highlighter-rouge">href=#</code> in each of these menu items to link to the appropriage html pages.</p>

<p>Next, take a look at other bootstrap features. Check out how to <a href="https://getbootstrap.com/docs/5.2/layout/columns/">create columns</a> without using tables as was done in the 90’s.</p>

<p>You may want to take a look at how to create <a href="https://getbootstrap.com/docs/5.2/content/images/">responsive images</a> that shrink and expand as the page size changes so they look good on any size device.</p>

<p>And while you are thinking about images for your homepage, check out how to create a <a href="https://getbootstrap.com/docs/5.2/components/carousel/">carousel</a> to automatically cycle through more than one image.</p>

<p>You are the designer, the design here is up to you. Have fun and see what you can create! A more recent RadioShack logo is included if you want to use it.</p>

<a data-id="" id="thought-question" style="top: 0px;"></a><h2><a data-id="" href="#thought-question">Thought Question</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Why do you think so many designers use Bootstrap, rather than creating their own CSS?</li>
</ul>

<a data-id="" id="how-to-test-your-code" style="top: 0px;"></a><h2><a data-id="" href="#how-to-test-your-code">How to Test Your Code</a></h2>

<p>No <code class="language-plaintext highlighter-rouge">check50</code> for this assignment! To ensure that the code on your pages is valid, you can use this <a href="https://validator.w3.org/#validate_by_input">Markup Validation Service</a>, copying and pasting your HTML directly into the provided text box.</p>

<a data-id="" id="how-to-submit" style="top: 0px;"></a><h2><a data-id="" href="#how-to-submit">How to Submit</a></h2>

<p>No need to submit! This is practice problem.</p>


   
