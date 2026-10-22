URL: https://support.mozilla.org/en-US/kb/report-breakage-due-blocking
Date: 2026-10-22

# How do I report a broken site in Firefox desktop?

Are you experiencing issues with a webpage that works fine in other browsers but not in Firefox? This could be a [web compatibility](https://www.techopedia.com/definition/23240/browser-compatibility) (webcompat) issue. Common signs include:

- Slow or non-functional sites

- Broken images or videos

- Malfunctioning buttons, links and text boxes

- Missing content

- Issues with signing in or password autofill

- Problems when using an ad blocker

To proactively combat these web compatibility issues, Firefox has integrated a user- friendly reporting tool directly into the browser. This tool enables users to swiftly report issues related to content blocking, thereby aiding in the enhancement of Firefox's performance and user experience.

To ensure your privacy, the reporting tool allows you to edit the URL before reporting, enabling you to remove any personal information from the URL. For detailed information and precautions, turn to the [Protect your information](https://support.mozilla.org/en-US/kb/report-breakage-due-blocking#w_protect-your-information) section detailed later in this article.

## How can I access the Report broken site tool?

If a site seems broken due to web compatibility or [Enhanced Tracking Protection](https://support.mozilla.org/en-US/kb/enhanced-tracking-protection-firefox-desktop)- related issues, you can report it directly to the Webcompat team. To report a site that isn’t working properly, follow these steps:

> **Note:** The reporting tool does not work from the New Tab page or on Firefox about: pages.

1. Go to the problem website.

2. At the top right, click the menu button to open the Firefox menu.

3. At the bottom of the menu, select the Help and Report option, then select Report Broken Site.

4. Review the site URL (which can be edited) and pick an option under What's not working?.

5. To submit your report, click the **Send report** button in the next panel that opens.

6. A success message will confirm your submission. To conclude, click the **Okay** button.

## What information does Mozilla collect from your report?

We wish to keep our process as transparent as possible. Any reports you send to Mozilla with this tool will include the following information when we receive it via our data pipeline:

- uuid: A single-use Unique User ID that helps us identify the specific report in our data pipeline. This is not tied to your Firefox profile in any way and cannot be used to identify you. If you submit multiple reports, it will be a different uuid each time.

- reported_at: The timestamp when our pipeline receives your report

- comments: Any notes you would like to share with us in the optional Describe the problem box.

- url = The URL of the site you are reporting. While the feature automatically populates the text field with the URL of the site you are currently on when you select Report Broken Site, you will be able to edit it prior to submitting the report.

- breakage_category = The answer you chose from the Choose reason dropdown menu

- details

- Device (Operating system, version, screen dimensions & touchscreen capability)

- User Agent String (Mozilla version, Gecko version, Firefox version and build date)

- Graphics (GPU model, version and rendering capabilities)

- Privacy settings

- If you’re submitting a report from a Private Browsing window

- If Firefox site isolation (Fission) is turned on

- If Total Cookie Protection is turned on

- Enhanced Tracking Protection (On, Off or Only in private browsing)

- Your protection level (Standard, Strict or Custom)

- Third-party tracking cookies (Blocked or Allowed)

- Which third-party tracking cookie block list is being used (Level 1 or 2)

- Fingerprinting (Blocked or Allowed)

- Cryptomining (Blocked or Allowed)

- Other third-party cookies (Always blocked, Never blocked or Blocked from unvisited websites)

- Custom referrer settings from about:config

- If cookies are set to expire at the end of your session

- How long third-party storage will be kept

- Security settings (Any antivirus software, antispyware or firewalls installed)

- Languages used for Firefox, and

- Any details you share in the optional Describe the problem text box

## Protect your information

**Customizable URL** The Report broken site tool pre-fills the URL of the site you're reporting. Beware, some URLs might contain sensitive data, such as shipping details or personal tax information. To protect your privacy, edit the URL to omit personal details. Note, however, that changes to the URL might hinder our issue reproduction efforts.

**OptionalDescribe the ProblemText Box** If you believe additional details in the Describe the Problem area could help resolve your web compatibility issue, feel free to include them. However, carefully consider the information you share. We implement measures to protect your data temporarily before it's securely discarded, but submitting sensitive information is ultimately your choice. Your contributions are crucial to our Webcompat team's efforts in improving Firefox. Providing extra context, including thorough responses to What’s broken?, aids us in identifying and rectifying major problems that negatively affect your browsing.

## What will Firefox do with your report?

When you submit a Report broken site form, the data is stored in a secure database. The Firefox Webcompat Team reviews these reports and makes an effort to remove data that might have been incidentally included in either the URL or the comments before sharing it with other Mozilla personnel involved in issue resolution. The team may use automated technologies, including third party services and LLMs, to assist with the translation, prioritization and resolution of these reviews. Data from your report is **not** used to train these models. As part of this issue resolution, Mozilla may file a bug in our

Bugzilla tool to help engineers diagnose and fix the issues identified; as a public platform, the submitted URLs within Bugzilla are publicly visible, but each submission is first manually reviewed to remove any identifiable information.

Mozilla also separately securely stores the submitted data for trend analysis and to compile aggregated user statistics. This data may also be shared with researchers on a de-identified or aggregated basis.

## Related content

To learn more about the privacy principles that guide Mozilla's mission, visit:

- [How to stay safe on the web](https://support.mozilla.org/en-US/kb/how-stay-safe-web)

- [Mozilla Privacy Policy](https://www.mozilla.org/privacy/)

- [Data Privacy Principles](https://www.mozilla.org/about/policy/lean-data/)

- [Firefox Privacy Notice](https://www.mozilla.org/privacy/firefox/)

- [Mozilla's Data Privacy FAQ](https://www.mozilla.org/privacy/faq/)
