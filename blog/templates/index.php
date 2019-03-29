{% extends "base.html" %}


{% block title %}WNIT - JSBLOG {% endblock %}

{% block logged_user %} 
{{ current_user }} 
{% endblock %}

{% block landing_page_services %}
<h2 class="s-title text-center-xs">We do it all..</h2>

							<div class="skills-items clearAfter">
								<div class="skills-item">
									<div class="skills-item-inside">
										<div class="skills-title">WEB Api</div>
										<div class="skills-desc">ASP.NET, Java, Ruby On Rails, Node.js, you name it...</div>
									</div>
								</div>
									<div class="skills-item">
									<div class="skills-item-inside">
										<div class="skills-title">MOBILE APPS</div>
										<div class="skills-desc">Android & iOS + React.js Native</div>
									</div>
								</div>
									<div class="skills-item">
									<div class="skills-item-inside">
										<div class="skills-title">FRONT-END</div>
										<div class="skills-desc">Angular.js, React.js, JS, CSS3, HTML5</div>
									</div>
								</div>
								<div class="skills-item">
                    <div class="skills-item-inside">
                        <div class="skills-title">CMS and SYSTEM INTEGRATIONS</div>
                        <div class="skills-desc">PHP, Wordpress, Magento, Marketing automation, etc.</div>
                    </div>
                </div>
                <div class="skills-item">
                    <div class="skills-item-inside">
                        <div class="skills-title">SERVER ADMINISTRATION</div>
                        <div class="skills-desc">Nginx, Linux, others</div>
                    </div>
                </div>
                <div class="skills-item">
                    <div class="skills-item-inside">
                        <div class="skills-title">DESIGN & USER EXPERIENCE</div>
                        <div class="skills-desc">Web design, UX consulting, testing and optimization</div>
                    </div>
                </div>
                <div class="skills-item">
                    <div class="skills-item-inside">
                        <div class="skills-title">MARKETING SERVICES</div>
                        <div class="skills-desc">SEO, SEM, copywriting</div>
                    </div>
                </div>
                <div class="skills-item">
                    <div class="skills-item-inside">
                        <div class="skills-title">(ALMOST) ANYTHING ELSE</div>
                        <div class="skills-desc">We tailor teams and services to your specific objectives</div>
                    </div>
                </div>
{% endblock %} 

{% block landing_page_services_next %}
			{% load static %}

 <section class="columns">
        <div class="container-fluid">
            <div class="row clearAfter">
                <div class="column clearAfter">
                    <div class="column-inside left center-xs">
                        <div class="column-img" style="background-image: url('{% static 'images/main1.jpg' %}');"></div>
                        <div class="column-bottom">
                            <div class="column-title">
                            By Project</div>
                            <div class="column-desc">Perfect for fixed-scope or fixed-budget engagements. We'll support you end-to-end, from documentation to delivery.</div>
                        </div>
                    </div>
                </div>
                <div class="column clearAfter">
                    <div class="column-inside center">
                        <div class="column-img" style="background-image: url('{% static 'images/main2.jpg' %}');"></div>
                        <div class="column-bottom">
                            <div class="column-title">By resource</div>
                            <div class="column-desc">If you prefer to manage your own developers or marketers, we'll connect you with the right talent and we'll take care of all the details.</div>
                        </div>
                    </div>
                </div>
                <div class="column clearAfter">
                    <div class="column-inside right-md center-xs">
                        <div class="column-img" style="background-image: url('{% static 'images/main3.jpg' %}');"></div>
                        <div class="column-bottom">
                            <div class="column-title">By dedicated team</div>
                            <div class="column-desc">Tailor-fit and independently-run development teams support you directly, allowing you to focus on your core competency.</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="clear"></div>
        </div>
    </section>

{% endblock %} 


{% block used_technologies %}
	<div id="idkwhat" class="s-title text-center-xs">Technologies used:</div>
		<div id="big-image"><a href="images/gallery/1.png" target="_blank"><img src="images/gallery/1.png" alt="1"></a></div>
		<div id="small-images">
			<div class="small-image">
				<a href="images/gallery/1.jpg" target="_blank"><img src="images/gallery/1.jpg" alt="JavaScript Angular Framework"></a>
			</div>
			<div class="small-image">
				<a href="images/gallery/2.jpg" target="_blank"><img src="images/gallery/2.jpg" alt="PHP Laravel Framework"></a>
			</div>
			<div class="small-image">
				<a href="images/gallery/3.jpg" target="_blank"><img src="images/gallery/3.jpg" alt="PHP Symphony Framework"></a>
			</div>
			<div class="small-image">
				<a href="images/gallery/4.jpg" target="_blank"><img src="images/gallery/4.jpg" alt="PHP YII Framework"></a>
			</div>
			<div class="small-image">
				<a href="images/gallery/5.jpg" target="_blank"><img src="images/gallery/5.jpg" alt="JavaScript Aurelia Framework"></a>
			</div>
			<div class="small-image">
				<a href="images/gallery/6.jpg" target="_blank"><img src="images/gallery/6.jpg" alt="JavaScript Backbone Framework"></a>
			</div>
			<div class="small-image">
				<a href="images/gallery/7.jpg" target="_blank"><img src="images/gallery/7.jpg" alt="Javascript Dojo Framework"></a>
			</div>
			<div class="small-image">
				<a href="images/gallery/8.jpg" target="_blank"><img src="images/gallery/8.jpg" alt="PHP Symphony Framework"></a>
			</div>
			<div class="small-image">
				<a href="images/gallery/9.jpg" target="_blank"><img src="images/gallery/9.jpg" alt="PHP Symphony Framework"></a>
			</div>
			<div class="small-image">
				<a href="images/gallery/10.jpg" target="_blank"><img src="images/gallery/10.jpg" alt="10"></a>
			</div>
			<div class="small-image">
				<a href="images/gallery/11.jpg" target="_blank"><img src="images/gallery/11.jpg" alt="11"></a>
			</div>
			<div class="small-image">
				<a href="images/gallery/12.jpg" target="_blank"><img src="images/gallery/12.jpg" alt="12"></a>
			</div>
		</div>
			</section>
		</div>

{% endblock %} 

{% block info %}




<li> siemanko </li>
<ol> ojejuniu</ol>
<li> xddd </li>

{% endblock info %}

{% block additional_js %}
{% load static %}
<script src="{% static 'js\js.js' %}"></script>

{% endblock additional_js %}

{% block javascript %}


{% endblock %}


{% block separator %}
			<section class="line-between-sections"></section>	
{% endblock %}