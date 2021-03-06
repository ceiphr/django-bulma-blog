# Ceiphr.com Changelog

All notable changes to the latest release of this project are documented in this post.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.3] - 2019-06-29

### Added

- Dribbble integration for a design page in the portfolio app
- Instagram integration for the photography page in the portfolio app
- Disqus integration for articles (click to load comments 
improved page performance)

### Security

- Replaced `frame-src` with `worker-src`
- Updated CSP to properly handle integration with Instagram and Disqus

## [0.2.2] - 2019-05-01

### Added

- Added darkmode Sass using `@media (prefers-color-scheme: dark)`
- DNS now handled by Cloudflare
- Added custom error pages for Cloudflare

### Changed

- Rebased from Gitlab to Github
- Replaced MaterializeCSS with Bulma
- Rewrote all Django templates
- Rewrote Sass files
- Rewrote part of models for blog posts and projects
- Split database app into portfolio and blog apps

### Removed

- Removed "Events" page
- Removed "Skills" page
- Removed "Contact" page
- Removed jQuery
- Removed SendGrid

### Security
- Added `'unsafe-eval'` and  `'unsafe-inline'` to `CSP_SCRIPT_SRC` so 
Cloudflare scripts can run in the browser

## [0.2.1] - 2019-03-30

### Added

- Carbon Ads integrated **on article template only** (Yaaaay!)
- Digital Ocean spaces CDN added under the `cdn` subdomain (i.e. [cdn.ceiphr.com](https://cdn.ceiphr.com))
- Article images are now interactive
- LaTeX support added
- Publish boolean added to articles so they can be previewed without showing up on the sitemap or on the site
- Added tagging system with filtered feed for blog articles
- Articles now have a tiny footer for tags and publishing details
- Sitemap.xml generation system

### Changed

- All fonts changed to the superior IBM Plex
- Integrated header image into the sites main header
- Skills now have categories
- Ordered and unordered list points are cleaner and more readable
- Blockquotes now act as *notice* blocks
- Reduced gzip level from 9 to 7
- Made margins more readable on articles
- All link text is now light-blue

### Removed

- Removed "Events" from front page

### Security

- Reduced SSL session caching time

## [0.2.0] - 2019-03-30

### Added

- Front page with a mixed feed from projects/blog/events tabs
- Blogging system added with markdown and syntax highlighting support
- "Changelog" tab dedicated to changes made to all of my side projects
- SendGrid added for handling the contact form's outgoing emails
- Fathom analytics (all data is handled by me on a self-hosted instance)
- Sitemap.xml generation system

### Changed

- All images are now optimized using the WebP image format
- All images have a fallback JPEG version (for Apple devices)
- Rain/title cover is centered properly
- Skills tab is now a table of skills with "experience" and "last used" columns
- Contact page form now has a "subject" field
- Contact page margins fit the form to the page on desktop
- A copy of the contact form submission is now sent to me and the user
- Backend now uses PostgresQL for its databasing solution
- README preview image updated
- README credits updated for new resources

### Removed

- Confidence system in skills

### Security

- Admin panel hidden with hashed URL
- Admin login requires TOTP
