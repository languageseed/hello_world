<script lang="ts">
  import { base } from '$app/paths';
  import { 
    Linkedin, 
    Briefcase, 
    Award, 
    Calendar, 
    MapPin, 
    ExternalLink,
    ChevronRight,
    Building2,
    Code,
    Server,
    Shield
  } from 'lucide-svelte';

  const experience = [
    {
      company: 'Mineral Resources Limited',
      role: 'Project Manager',
      type: 'Full-time',
      period: 'Dec 2023 - Present',
      duration: '2+ years',
      location: 'Australia · On-site',
      highlights: [
        'Network Carrier Services and SDWAN',
        'IT Disaster Recovery Project',
        'MRT Weipa, QLD',
        'Rubrik Secure Cloud'
      ]
    },
    {
      company: 'Datacom',
      role: 'Project Manager',
      type: 'Full-time',
      period: 'May 2015 - Nov 2023',
      duration: '8 yrs 7 mos',
      location: 'Greater Perth Area · Hybrid',
      highlights: [
        'Data Centre Relocation and Decommissioning',
        'Network, Firewall, Loadbalancer, Application Delivery',
        'Compute and Storage Infrastructure Refresh',
        'Virtual Infrastructure Migration',
        'Backup, Recovery and Disaster Recovery'
      ],
      initiatives: [
        'Bunnings Oracle Cloud Infrastructure Migration',
        'Bunnings Data Centre Relocation Program',
        'Datacom GovNext Service Tower Establishment',
        'Tianqi Lithium Corporate and NPI IT Establishment'
      ],
      technologies: [
        'Microsoft Azure', 'Oracle Cloud Infrastructure', 'Cisco ACI', 
        'Palo Alto Firewalls', 'F5 Load Balancing', 'VMware', 'Rubrik'
      ]
    },
    {
      company: 'Self-Employed Contractor',
      role: 'Project Manager',
      type: 'Contract',
      period: 'Mar 2013 - May 2015',
      duration: '2 yrs 3 mos',
      location: 'Greater Perth Area',
      highlights: [
        'Public cloud transition for small and medium business',
        'Application development for Mobile, Storefronts, xRM',
        'Enterprise telephony and contact centre solutions',
        'Business Continuity Management and Disaster Recovery'
      ]
    },
    {
      company: 'AusGroup Limited',
      role: 'Project Manager',
      type: 'Full-time',
      period: 'Feb 2012 - Nov 2012',
      duration: '10 mos',
      location: 'Greater Perth Area',
      highlights: [
        'Microsoft Lync Enterprise Voice and Collaboration',
        'Oracle Primavera P6 Enterprise Portfolio Management',
        'Business case development and requirements analysis'
      ]
    },
    {
      company: 'Wood Group',
      role: 'Solution Architect / Project Manager',
      type: 'Full-time',
      period: 'May 2011 - Nov 2011',
      duration: '7 mos',
      location: 'Greater Perth Area',
      highlights: [
        'SharePoint ECM Solutions',
        'SharePoint Custom Applications',
        'Microsoft Project Reporting Customisation'
      ]
    },
    {
      company: 'Datacom',
      role: 'Project Manager',
      type: 'Full-time',
      period: 'Nov 2008 - Apr 2011',
      duration: '2 yrs 6 mos',
      location: 'Greater Perth Area',
      highlights: [
        'Enterprise Document and Records Management',
        'VMware infrastructure',
        'Wide Area Networking and MPLS solutions',
        'IT Managed Services Transitions'
      ]
    },
    {
      company: 'DVG Automotive Group',
      role: 'IT Manager',
      type: 'Full-time',
      period: 'Nov 1999 - Nov 2008',
      duration: '9 yrs 1 mo',
      location: 'Greater Perth Area',
      highlights: [
        'Managed IT services for 20 franchises and 400 users',
        'Led small team for support and systems management',
        'Acquisitions and dealership IT integration',
        'Vendor management for automotive, finance, and insurance partners'
      ]
    }
  ];

  const certifications = [
    { name: 'PMI Professional in Business Analysis (PMI-PBA)', issuer: 'Project Management Institute', date: 'Dec 2022', id: '3379652' },
    { name: 'PMI Agile Certified Practitioner (PMI-ACP)', issuer: 'Project Management Institute', date: 'Aug 2021', id: '1862828E8' },
    { name: 'Certified Scrum Master', issuer: 'Scrum Alliance', date: 'Nov 2018', id: '857915' },
    { name: 'Managing Successful Programmes (MSP)', issuer: 'APMG International', date: 'Mar 2017', id: '1000536597' },
    { name: 'Project Management Professional (PMP)', issuer: 'Project Management Institute', date: 'Mar 2014', id: '1702880' },
    { name: 'ITIL v3 Foundations', issuer: 'APMG International', date: 'May 2012', id: 'ITIL/AU002508' },
    { name: 'PRINCE2 Practitioner', issuer: 'APMG International', date: 'Nov 2010', id: 'P2R/A53932' }
  ];

  const skills = [
    { category: 'Project Management', items: ['Agile/Scrum', 'Waterfall', 'PRINCE2', 'MSP', 'PMP'] },
    { category: 'Cloud & Infrastructure', items: ['Azure', 'Oracle Cloud', 'VMware', 'Hyper-V', 'Data Centre'] },
    { category: 'Networking & Security', items: ['Cisco ACI', 'Palo Alto', 'F5', 'SDWAN', 'Firewalls'] },
    { category: 'Business Analysis', items: ['Requirements', 'Business Cases', 'Process Improvement', 'Solution Assurance'] }
  ];
</script>

<svelte:head>
  <title>About - Ben McIntyre | Project Manager & AI Enthusiast</title>
  <meta name="description" content="Ben McIntyre - Project Manager with 20+ years experience in IT infrastructure, cloud migration, and enterprise solutions." />
</svelte:head>

<div class="max-w-5xl mx-auto px-6 py-12">
  <!-- Header -->
  <div class="text-center mb-12">
    <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 border border-primary/20 mb-6">
      <Briefcase class="w-4 h-4 text-primary" />
      <span class="text-sm font-medium text-primary">Career Profile</span>
    </div>
    <h1 class="font-display text-4xl md:text-5xl font-bold mb-4">
      Ben McIntyre
    </h1>
    <p class="text-xl text-foreground/70 mb-6">
      Project Manager · Business Analyst · AI Enthusiast
    </p>
    <a 
      href="https://www.linkedin.com/in/benmcintyre/" 
      target="_blank" 
      rel="noopener noreferrer"
      class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#0A66C2] text-white font-semibold hover:bg-[#004182] transition-all shadow-lg"
    >
      <Linkedin class="w-5 h-5" />
      Connect on LinkedIn
      <ExternalLink class="w-4 h-4" />
    </a>
  </div>

  <!-- Summary -->
  <section class="card-interactive p-8 mb-12">
    <p class="text-lg text-foreground/90 leading-relaxed">
      With over <strong>20 years of experience</strong> in IT project management, I've led complex infrastructure projects 
      across data centre migrations, cloud transformations, enterprise networking, and disaster recovery. 
      Currently exploring <strong>AI/ML infrastructure</strong> and building intelligent systems in my home lab.
    </p>
  </section>

  <!-- Skills Grid -->
  <section class="mb-12">
    <h2 class="font-display text-2xl font-bold mb-6 flex items-center gap-2">
      <Code class="w-6 h-6 text-primary" />
      Core Competencies
    </h2>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
      {#each skills as skill}
        <div class="card-interactive p-5">
          <h3 class="font-semibold text-primary mb-3">{skill.category}</h3>
          <div class="flex flex-wrap gap-2">
            {#each skill.items as item}
              <span class="px-2 py-1 text-xs rounded-full bg-secondary text-secondary-foreground">
                {item}
              </span>
            {/each}
          </div>
        </div>
      {/each}
    </div>
  </section>

  <!-- Experience Timeline -->
  <section class="mb-12">
    <h2 class="font-display text-2xl font-bold mb-6 flex items-center gap-2">
      <Building2 class="w-6 h-6 text-primary" />
      Experience
    </h2>
    <div class="space-y-6">
      {#each experience as job, index}
        <div class="card-interactive p-6 relative">
          <!-- Timeline connector -->
          {#if index < experience.length - 1}
            <div class="absolute left-8 top-full w-0.5 h-6 bg-border" />
          {/if}
          
          <div class="flex flex-col md:flex-row md:items-start gap-4">
            <div class="flex-shrink-0 w-12 h-12 rounded-xl bg-primary/10 flex items-center justify-center">
              <Briefcase class="w-6 h-6 text-primary" />
            </div>
            
            <div class="flex-1">
              <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-2 mb-2">
                <div>
                  <h3 class="font-display text-xl font-bold">{job.role}</h3>
                  <p class="text-primary font-medium">{job.company}</p>
                </div>
                <div class="text-sm text-muted-foreground text-right">
                  <div class="flex items-center gap-1">
                    <Calendar class="w-4 h-4" />
                    {job.period}
                  </div>
                  <div class="flex items-center gap-1">
                    <MapPin class="w-4 h-4" />
                    {job.location}
                  </div>
                </div>
              </div>
              
              <ul class="mt-3 space-y-1">
                {#each job.highlights as highlight}
                  <li class="flex items-start gap-2 text-sm text-foreground/80">
                    <ChevronRight class="w-4 h-4 text-primary flex-shrink-0 mt-0.5" />
                    {highlight}
                  </li>
                {/each}
              </ul>
              
              {#if job.technologies}
                <div class="mt-4 flex flex-wrap gap-1">
                  {#each job.technologies as tech}
                    <span class="px-2 py-0.5 text-xs rounded-full bg-secondary/50 text-muted-foreground">
                      {tech}
                    </span>
                  {/each}
                </div>
              {/if}
            </div>
          </div>
        </div>
      {/each}
    </div>
  </section>

  <!-- Certifications -->
  <section class="mb-12">
    <h2 class="font-display text-2xl font-bold mb-6 flex items-center gap-2">
      <Award class="w-6 h-6 text-primary" />
      Certifications
    </h2>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      {#each certifications as cert}
        <div class="card-interactive p-5 flex items-start gap-4">
          <div class="flex-shrink-0 w-10 h-10 rounded-lg bg-amber-500/10 flex items-center justify-center">
            <Award class="w-5 h-5 text-amber-500" />
          </div>
          <div>
            <h3 class="font-semibold text-foreground">{cert.name}</h3>
            <p class="text-sm text-muted-foreground">{cert.issuer}</p>
            <p class="text-xs text-muted-foreground mt-1">Issued {cert.date} · ID: {cert.id}</p>
          </div>
        </div>
      {/each}
    </div>
  </section>

  <!-- CTA -->
  <section class="text-center">
    <div class="card-interactive p-8 bg-gradient-to-br from-primary/5 to-primary/10">
      <h2 class="font-display text-2xl font-bold mb-4">Let's Connect</h2>
      <p class="text-foreground/70 mb-6 max-w-lg mx-auto">
        Interested in discussing project management, AI infrastructure, or potential collaborations?
      </p>
      <a 
        href="https://www.linkedin.com/in/benmcintyre/" 
        target="_blank" 
        rel="noopener noreferrer"
        class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-primary text-primary-foreground font-semibold hover:scale-105 transition-all shadow-lg shadow-primary/25"
      >
        <Linkedin class="w-5 h-5" />
        View Full Profile on LinkedIn
        <ExternalLink class="w-4 h-4" />
      </a>
    </div>
  </section>
</div>
