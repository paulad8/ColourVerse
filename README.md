# ART SPACE
### Get inspired by the masters of art history
***
*Developed by Paula De Amicis*

Code Institute's Milestone Project 3 culminates in completing all modules in the Full-stack Development journey. 
Drawing knowledge from HTML5, CSS3, JavaScript, SQLite, GitHub, Python and Django.
<Visit live website>

<Insert composite image of game screenshots>

### TABLE OF CONTENTS
1. Project Objective
2. Project Concept
3. User Objectives
4. Site Owner Objectives
5. User Experience
6. Design
7. Structure
8. Technologies Used
9. Testing
10. Credits
    
***

### PROJECT OBJECTIVE
To create a website with a single main page displaying randomly selected images removed from a separate portfolio page. 

### PROJECT CONCEPT
Art Space is an interactive, visually appealling online gallery that showcases a selection of pioneering artists, their artworks, and the movements they belong to. It offers an intuitive way for users to explore and discover art through search functionality, detailed artist and artwork pages, and categorised movements. The platform prioritises: 
- A clean and consistent design aligned with modern web standards.
- Responsive layouts to ensure a seamless experience across devices.
- Efficient search capabilities for users to find information by artist, movement or medium.
- Modularity and scalability to accommodate future enhancements, such as adding more artists, artworks, 

#### USER OBJECTIVES
The primary objectives of users interacting with this site would include:

1. Discovering and Exploring Artists
- Users can browse and learn about artists from different regions, movements, and mediums.
- Access detailed biographies, associated artworks, and related movements.
2. Exploring Artworks
- View high-quality images of artworks organized by medium, movement, or artist.
- Access comprehensive details about each artwork, including its title, medium, and movement.
3. Understanding Art Movements
- Explore various art movements through curated descriptions and visuals.
- Discover artworks and artists associated with each movement for better context and understanding.
4. Searching and Filtering
- Utilize the search bar to find artists, movements, or artworks by keyword.
- Filter content by medium, movement, or artist to quickly locate specific interests.
5. Enjoying a Visually Rich Experience
- Navigate a design-focused and visually engaging interface.
- Experience modal image pop-ups for detailed artwork viewing.
6. Accessing a User-Friendly and Responsive Platform
- Seamlessly interact with the site across devices, ensuring a consistent experience on desktops, tablets, and mobile phones.
- Explore an intuitive layout that simplifies navigation for both casual browsers and art enthusiasts.


#### SITE OWNER OBJECTIVES
- Demonstrate competency in the languages and frameworks studied under the Full Stack Development journey
- Create an artwork repository that is compelling and engaging and effectively applies modern UI standards and UX principles. 
- Design a visually appealing, fully responsive and accessible website
- Challenge myself by incorporating newly acquired programming knowledge with my design background,

And, 
- Art is for everybody.
- Art is to inspire.
- Art is joy.
- I am bringing key movements in art history and pioneering masters to the user. To move, to inspire, to educate.  

***
### USER EXPERIENCE
#### TARGET AUDIENCE
This project is designed to be a resourceful tool for art enthusiasts, researchers, and educators while also celebrating the diversity of artistic expression through a thoughtfully curated online experience.

#### USER REQUIREMENTS
- Simple navigation
- Logical presentation and flow of content 
- Responsive website that allows users to view and interact on any device
- Meets W3C accessibility standards to ensure the site works equally for everyone
- No broken code

***

### DESIGN


#### COLOUR PALETTE 
Consistent across all devices, to complement and not compete with the artworks on display, I have chosen a background with a gradient of soft, muted hues of lavender and pink. Components complement in purple with a similar subtle range of interaction states.


#### TYPOGRAPHY
Google Fonts are incorporated into the website: **Major Mono Display** for the heading and subheadings and **Poppins** for all other scales with a standard sans serif fallback. Major Mono Display was selected to reflect the site's arty aspect, while Poppins is legible and clear. 

#### PROTOTYPES
Wireframes, concept prototypes and user journeys were mapped out using [Figma](https://www.figma.com "Figma home"). 
   
![insert image here]

### STRUCTURE
The site is organised into several key sections, each designed to provide users with an intuitive way to navigate and explore the gallery's content: 
1. Home page
   - A welcoming introduction to the gallery,
   - Highlights key features such as search functionality,
   - Provides easy access to the primary navigation menu.
2. Random Artworks
   - Entering the gallery, the user is greeted by a display of randomly selected artworks that, when clicked, will open to the Artwork detail page.
3. Artist Detail page:
   - Offers in-depth information about the artist, including:
     - Biography,
     - Region,
     - Associated artworks and movements,
     - Media used in their artworks
4. Artist Overview page: 
   - Displays a grid of artists with their names and portraits (if available)
5. Artworks
   - Search Results: Displays all artworks categorised by a specific medium.
   - Includes high-resolution images, titles and links to associated artist and movement pages.
6. Movements
    - Overview Page: Showcases all art movements with their associated images and brief descriptions
    - Movement Detail page: Provides detailed information about the movement, including:
      - Historical context,
      - Associated artists and artworks,
      - Prominent styles and characteristics
7. Search Functionality
   - A dynamic search bar in the site's navigation allows users to find artists, movements and artworks by keywords.
   - Results are categorised for ease of navigation:
      - Artists (names listed),
      - Movements (images)
      - Artworks (images)
8. Modal View
   - Enables users to view artwork images in a larger format,
   - Displays additional details such as the title and artist, without leaving the current page.
9. Responsive Design
   - The site is fully responsive, ensuring an optimal vieweing experience across all devices,
   - Grids, images and navigation adapt seamlessly to different screen sizes, from desktops to tablets and mobile phones. 

   ***
### TECHNOLOGIES USED
The development of this website employed a variety of modern tools, technologies, and frameworks to ensure a seamless, visually appealing, and responsive user experience. 
Here's an overview of the technologies used:
- Django: A Python-based web framework for building robust, scalable web applications.
- SQLite: Used as the database during developments for storing data related to artists, artworks, movements and media. 
- HTML5: Forms the backbone of the site structure
- CSS3: Used to style the site, ensuring visual consistency and responsiveness. Key CSS features include:
  - Grid layout for arranging content,
  - Flexbox for flexible and adaptive UI components,
  - Custom CSS for a bespoke approach to styling to ensure a unique aesthetic consistent with the gallery's theme, avoiding heavy reliance on pre-built frameworks like Bootstrap, 
  - Media queries for responsive design
- Javascript: Adds interactivity, including modal functionality for viewing larger images and the dynamic search experience.
- Font Awesome: For icons and other visual elements. 

#### FRAMEWORKS, LIBRARIES & TOOLS
- <composite image> to create the multi-device mock-up 
- [Figma](https://www.figma.com "Figma home") - used to map out concept
- [Favicon](https://favicon.io/ "Favicon home") - to create the Favicon
- [PyCharm]- chosen IDE
- [GitHub](https://github.com/ "GitHub home") - version control
- [GitHub Desktop](https://desktop.github.com/ "GitHub Desktop home") - to push changes and simplify development workflow
- [AWS Elastic Beanstalk](https://signin.aws.amazon.com/signup?request_type=register) - deployment and hosting
- [a11y](https://color.a11y.com/Contrast/ "a11y Contrast checker") - colour contrast accessibility validator
- [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/ "Google Chrome Developer") - to test responsiveness and debug
- [Mobile simulator](https://chrome.google.com/webstore/detail/mobile-simulator-responsi/ckejmhbmlajgoklhgbapkiccekfoccmk "Mobile simulator extension overview") - to test responsiveness on a vast range of devices. 
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/ "Lighthouse overview") - used to audit performance, accessibility, development best-practice and SEO. 
***

### TESTING
Testing was an integral part of the development process to ensure the website's functionality, performance, and user experience met the project objectives. Here's an overview of the testing approaches used: 
###1. Manual Testing
- Cross-Browser Compatibility: The site was tested on popular web browsers, including Chrome, Firefox and Safari to ensure consistent functionality and styling.
- Device Responsiveness: The design was evaluated on various devies, such as desktops, tablets and smartphones to confirm responsiveness and usability across screen sizes.
- Navigation: Tested links, menus and buttons for accessibility and proper routing to ensure seamless user interaction.
- Search Functionality: Verified that the search bar returned correct results for artists, movements and media, and displayed them appropriately.

### 2. Functionality Testing
- Image Upload and Display: Confirmed that uploaded images (artists, movements, artworks) were stored correctly and displayed in the appropriate sections.
- Dynamic Content Rendering: Checked the correct association and display of artists, artworks, and movements across the site.
- Forms: Ensured forms (e.g., search bar) handled user input correctly, including edge cases such as invalid or missing input.

### 3. PERFORMANCE TESTING 
- Loading Times: Evaluated the speed of page loads, especially for image-heavy sections, to optimize user experience.
- Database Queries: Used Django Debug Toolbar to identify and optimize slow or redundant database queries.

### 4. CODE TESTING
- Python and Django Debugging Tools: Used Django's built-in error reporting to troubleshoot and resolve backend issues.

## DEPLOYMENT
This website was deployed to AWS Elastic Beanstalk 
***

### CREDITS
- Fonts from [Google Fonts](https://fonts.google.com/)
- HTML icons from [Font Awesome](https://fontawesome.com/)
- [Favicon](https://favicon.io/favicon-converter/) converted icon created by Vectors Market on [Flaticon](https://www.flaticon.com/free-icons/travel) 
- Code snippets, guidance and inspiration from the broader online code community via [StackOverflow](https://stackoverflow.com/)





