---
layout: page
title: Privacy Policy
---
<div class="col-lg-12 text-center">
	<h2 class="section-heading text-uppercase">Privacy Policy</h2>
</div>

This Privacy Policy describes how your personal information is collected, used, and shared when you visit {{ site.title }} (the "Site").

**PERSONAL INFORMATION WE COLLECT**

**Contact Form Information:**
When you use the contact form on this website, we collect the information you provide, including:
- Your name
- Your email address
- Your phone number (optional)
- Your message content

This information is processed through Formspree, a third-party service that handles form submissions. Formspree's privacy policy can be found at: <https://formspree.io/legal/privacy-policy/>.

**Automatically Collected Information:**
{% if site.analytics.google %}
When you visit the Site, we automatically receive information about your device from your browser, such as your IP address. As you browse the Site, we also collect information about how you interact with the Site. We refer to this automatically-collected information as "Device Information".

We collect Device Information using Google Analytics. "Cookies" are data files that are placed on your device. For more information about cookies and how to disable them, visit http://www.allaboutcookies.org.

Google Analytics Privacy Policy: <https://www.google.com/intl/en/policies/privacy/>.

You can opt-out of Google Analytics here: <https://tools.google.com/dlpage/gaoptout>.
{% else %}
We do not collect any additional data about you or use any cookies beyond what is necessary for the website to function.
{% endif %}

**HOW WE USE YOUR INFORMATION**

We use the information we collect to:
- Respond to your contact form submissions
- Improve the website's functionality and user experience
- Analyze website traffic and usage patterns (if analytics are enabled)
- Comply with legal obligations

**INFORMATION SHARING**

We do not sell, trade, or otherwise transfer your personal information to third parties except:
- Formspree (for contact form processing)
- {% if site.analytics.google %}Google Analytics (for website analytics){% endif %}
- When required by law or to protect our rights

**DATA RETENTION**

- Contact form submissions are stored by Formspree according to their retention policies
- {% if site.analytics.google %}Analytics data is retained according to Google Analytics policies{% endif %}
- You may request deletion of your data by contacting us

**YOUR RIGHTS**

You have the right to:
- Request access to your personal information
- Request correction of inaccurate information
- Request deletion of your personal information
- Opt-out of analytics tracking (if applicable)

**SECURITY**

We implement appropriate security measures to protect your personal information. However, no method of transmission over the internet is 100% secure.

**THIRD-PARTY SERVICES**

This website uses the following third-party services:
- **Formspree**: For contact form processing
- {% if site.analytics.google %}**Google Analytics**: For website analytics{% endif %}
- **GitHub Pages**: For website hosting

Each service has its own privacy policy and data handling practices.

**CHANGES TO THIS POLICY**

We may update this privacy policy from time to time for personal, operational, legal, or regulatory reasons. We will notify you of any material changes by posting the new policy on this page.

**CONTACT US**

For more information about our privacy practices or if you have questions, please contact us by email at <a href="mailto:{{ site.email }}">{{ site.email }}</a>.

**Last Updated:** {{ site.time | date: "%B %d, %Y" }}
