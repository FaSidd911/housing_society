/**
* Template Name: Ninestars
* Updated: Mar 10 2023 with Bootstrap v5.2.3
* Template URL: https://bootstrapmade.com/ninestars-free-bootstrap-3-theme-for-creative/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let header = select('#header')
    let offset = header.offsetHeight

    let elementPos = select(el).offsetTop
    window.scrollTo({
      top: elementPos - offset,
      behavior: 'smooth'
    })
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function(e) {
    select('#navbar').classList.toggle('navbar-mobile')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })

  /**
   * Mobile nav dropdowns activate
   */
  on('click', '.navbar .dropdown > a', function(e) {
    if (select('#navbar').classList.contains('navbar-mobile')) {
      e.preventDefault()
      this.nextElementSibling.classList.toggle('dropdown-active')
    }
  }, true)

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on('click', '.scrollto', function(e) {
    if (select(this.hash)) {
      e.preventDefault()

      let navbar = select('#navbar')
      if (navbar.classList.contains('navbar-mobile')) {
        navbar.classList.remove('navbar-mobile')
        let navbarToggle = select('.mobile-nav-toggle')
        navbarToggle.classList.toggle('bi-list')
        navbarToggle.classList.toggle('bi-x')
      }
      scrollto(this.hash)
    }
  }, true)

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash)
      }
    }
  });

  /**
   * Porfolio isotope and filter
   */
  window.addEventListener('load', () => {
    let portfolioContainer = select('.portfolio-container');
    if (portfolioContainer) {
      let portfolioIsotope = new Isotope(portfolioContainer, {
        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
      });

      let portfolioFilters = select('#portfolio-flters li', true);

      on('click', '#portfolio-flters li', function(e) {
        e.preventDefault();
        portfolioFilters.forEach(function(el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');

        portfolioIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        portfolioIsotope.on('arrangeComplete', function() {
          AOS.refresh()
        });
      }, true);
    }

  });

  /**
   * Initiate portfolio lightbox 
   */
  const portfolioLightbox = GLightbox({
    selector: '.portfolio-lightbox'
  });

  /**
   * Portfolio details slider
   */
  new Swiper('.portfolio-details-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });

  /**
   * Clients Slider
   */
  new Swiper('.clients-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 2,
        spaceBetween: 40
      },
      480: {
        slidesPerView: 3,
        spaceBetween: 60
      },
      640: {
        slidesPerView: 4,
        spaceBetween: 80
      },
      992: {
        slidesPerView: 6,
        spaceBetween: 120
      }
    }
  });

  /**
   * Animation on scroll
   */
  window.addEventListener('load', () => {
    AOS.init({
      duration: 1000,
      easing: "ease-in-out",
      once: true,
      mirror: false
    });
  });

  /*
	    Sidebar
	*/
      $('.dismiss, .overlay').on('click', function() {
        $('.sidebar').removeClass('active');
        $('.overlay').removeClass('active');
    });

    $('.open-menu').on('click', function(e) {
      e.preventDefault();
        $('.sidebar').addClass('active');
        $('.overlay').addClass('active');
        // close opened sub-menus
        $('.collapse.show').toggleClass('show');
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    });
    /* change sidebar style */
    $('a.btn-customized-dark').on('click', function(e) {
    e.preventDefault();
    $('.sidebar').removeClass('light');
    });
    $('a.btn-customized-light').on('click', function(e) {
    e.preventDefault();
    $('.sidebar').addClass('light');
    });
    /* replace the default browser scrollbar in the sidebar, in case the sidebar menu has a height that is bigger than the viewport */
    $('.sidebar').mCustomScrollbar({
    theme: "minimal-dark"
    });


})()

$("#toggleID").on("click", function() {
  $(this).toggleClass('orange');
});


/*
	    Get Aria Toggle Value
	*/

  function Water_Charges() {document.getElementById("Water_Charges").value = document.getElementById("Water_Charges_btn").getAttribute('aria-pressed');}
  function Municipal_Tax() {document.getElementById("Municipal_Tax").value = document.getElementById("Municipal_Tax_btn").getAttribute('aria-pressed');}
  function Maintainance_Charges() {document.getElementById("Maintainance_Charges").value = document.getElementById("Maintainance_Charges_btn").getAttribute('aria-pressed');}
  function Interest_from_Bank_Savings_Account() {document.getElementById("Interest_from_Bank_Savings_Account").value = document.getElementById("Interest_from_Bank_Savings_Account_btn").getAttribute('aria-pressed');}
  function Membership_Subscription_Charges() {document.getElementById("Membership_&_Subscription_Charges").value = document.getElementById("Membership_&_Subscription_Charges_btn").getAttribute('aria-pressed');}
  function Audit_Fees() {document.getElementById("Audit_Fees").value = document.getElementById("Audit_Fees_btn").getAttribute('aria-pressed');}
  function Staff_Welfare() {document.getElementById("Staff_Welfare").value = document.getElementById("Staff_Welfare_btn").getAttribute('aria-pressed');}
  function Accounting_Charges() {document.getElementById("Accounting_Charges").value = document.getElementById("Accounting_Charges_btn").getAttribute('aria-pressed');}
  function Postage_Courier_Charges() {document.getElementById("Postage_&_Courier_Charges").value = document.getElementById("Postage_&_Courier_Charges_btn").getAttribute('aria-pressed');}
  function Repair_Maintainence_Electrical() {document.getElementById("Repair_&_Maintainence_Electrical").value = document.getElementById("Repair_&_Maintainence_Electrical_btn").getAttribute('aria-pressed');}
  function Depreciation() {document.getElementById("Depreciation").value = document.getElementById("Depreciation_btn").getAttribute('aria-pressed');}
  function Meeting_Expenses() {document.getElementById("Meeting_Expenses").value = document.getElementById("Meeting_Expenses_btn").getAttribute('aria-pressed');}
  function Telephone_Charges() {document.getElementById("Telephone_Charges").value = document.getElementById("Telephone_Charges_btn").getAttribute('aria-pressed');}
  function Electricity_Charges() {document.getElementById("Electricity_Charges").value = document.getElementById("Electricity_Charges_btn").getAttribute('aria-pressed');}
  function Security_Charges() {document.getElementById("Security_Charges").value = document.getElementById("Security_Charges_btn").getAttribute('aria-pressed');}
  function Printing_Stationary() {document.getElementById("Printing_&_Stationary").value = document.getElementById("Printing_&_Stationary_btn").getAttribute('aria-pressed');}
  function Repair_Maintainence() {document.getElementById("Repair_&_Maintainence").value = document.getElementById("Repair_&_Maintainence_btn").getAttribute('aria-pressed');}
  function Conveyance() {document.getElementById("Conveyance").value = document.getElementById("Conveyance_btn").getAttribute('aria-pressed');}
  function Gardening_Expenses() {document.getElementById("Gardening_Expenses").value = document.getElementById("Gardening_Expenses_btn").getAttribute('aria-pressed');}
  function Bank_Charges() {document.getElementById("Bank_Charges").value = document.getElementById("Bank_Charges_btn").getAttribute('aria-pressed');}
  function Plumbing_Expenses() {document.getElementById("Plumbing_Expenses").value = document.getElementById("Plumbing_Expenses_btn").getAttribute('aria-pressed');}
  function Salary_to_Staff() {document.getElementById("Salary_to_Staff").value = document.getElementById("Salary_to_Staff_btn").getAttribute('aria-pressed');}
  function Service_Charges() {document.getElementById("Service_Charges").value = document.getElementById("Service_Charges_btn").getAttribute('aria-pressed');}
  function Sinking_Funds() {document.getElementById("Sinking_Funds").value = document.getElementById("Sinking_Funds_btn").getAttribute('aria-pressed');}
  function Repair_Funds() {document.getElementById("Repair_Funds").value = document.getElementById("Repair_Funds_btn").getAttribute('aria-pressed');}
  function Parking_Charges() {document.getElementById("Parking_Charges").value = document.getElementById("Parking_Charges_btn").getAttribute('aria-pressed');}
  function Property_Tax() {document.getElementById("Property_Tax").value = document.getElementById("Property_Tax_btn").getAttribute('aria-pressed');}
  function Miscellaneous_Charges() {document.getElementById("Miscellaneous_Charges").value = document.getElementById("Miscellaneous_Charges_btn").getAttribute('aria-pressed');}
  function Water_Charges_Paid() {document.getElementById("Water_Charges_Paid").value = document.getElementById("Water_Charges_Paid_btn").getAttribute('aria-pressed');      }