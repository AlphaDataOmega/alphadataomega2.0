#!/usr/bin/env python3
"""
Script to concatenate all project-overview documents into PROJECT_OVERVIEW_v2.md
Creates a complete, properly formatted overview document.
"""

import os
from pathlib import Path
from datetime import datetime

def main():
    # Define paths
    project_overview_dir = Path("/home/ubuntu/alphadataomega/docs/project-overview")
    output_file = Path("/home/ubuntu/alphadataomega/PROJECT_OVERVIEW_v2.md")
    
    # Get all numbered markdown files and sort them
    md_files = []
    for i in range(1, 21):  # Files 01 through 20
        pattern = f"{i:02d}_*.md"
        matches = list(project_overview_dir.glob(pattern))
        if matches:
            md_files.append(matches[0])
        else:
            print(f"Warning: No file found matching pattern {pattern}")
    
    print(f"Found {len(md_files)} project overview files to concatenate:")
    for file in md_files:
        print(f"  - {file.name}")
    
    # Create the concatenated content
    lines = []
    
    # Add comprehensive header
    lines.extend([
        "# AlphaDataOmega (ADO) & TRN Platform - Complete Project Overview v2.0",
        "",
        f"*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*",
        "",
        "## About This Document",
        "",
        "This comprehensive overview synthesizes insights from 20 strategic discussions and detailed",
        "project analysis covering AlphaDataOmega's complete ecosystem architecture, from immediate",
        "technical implementation to multi-generational civilizational impact.",
        "",
        "**Project Scope:** 4 parallel projects (CHAIN, ADO, DAOs, TRN) developed simultaneously",
        "**Development Timeline:** 32-week parallel sprint to production deployment", 
        "**Vision:** Digital sovereignty infrastructure for creator economy and cosmic consciousness",
        "",
        "---",
        "",
        "## Table of Contents",
        ""
    ])
    
    # Add table of contents
    toc_entries = [
        "1. Introduction and Vision",
        "2. User Sovereignty and Recovery", 
        "3. Architecture and Technical Stack",
        "4. AI Memory and Quantum Security",
        "5. Layer Interactions and Data Storage",
        "6. Governance and Tokens",
        "7. Token Mechanics and Council Governance",
        "8. Token Supply and Fractionalization", 
        "9. Engagement and Moderation Systems",
        "10. Moderation and Geolocation Systems",
        "11. Lottery and Vault Systems",
        "12. Subscription and UI Systems",
        "13. Onboarding and Streaming",
        "14. Anonymous Mode and Accessibility",
        "15. UX Metrics and Risk Management",
        "16. Security and Economic Simulations",
        "17. Compliance and AI Fairness",
        "18. Team Resources and Build Deployment",
        "19. Milestones and Success Metrics",
        "20. Legacy Planning and Community Involvement"
    ]
    
    for entry in toc_entries:
        lines.append(f"- {entry}")
    
    lines.extend([
        "",
        "---",
        ""
    ])
    
    # Process each file
    for i, file_path in enumerate(md_files, 1):
        print(f"Processing {file_path.name}...")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue
        
        # Add section header
        section_title = toc_entries[i-1] if i <= len(toc_entries) else f"Section {i}"
        lines.extend([
            f"<a id=\"section-{i:02d}\"></a>",
            f"<!-- ==================== SECTION {i:02d}: {section_title} ==================== -->",
            "",
        ])
        
        # Add the content
        lines.append(content)
        lines.extend([
            "",
            "---",
            ""
        ])
    
    # Add footer
    lines.extend([
        "## Document Information",
        "",
        f"- **Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- **Total Sections:** {len(md_files)}",
        "- **Source:** /docs/project-overview/ directory",
        "- **Version:** 2.0",
        "",
        "---",
        "",
        "*This document represents the complete AlphaDataOmega project overview,*", 
        "*synthesizing technical implementation with multi-generational vision.*",
        "",
        "**AlphaDataOmega: Where today's creator economy meets tomorrow's cosmic civilization.**"
    ])
    
    # Write the file
    final_content = "\n".join(lines)
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        print(f"\n✅ Successfully created {output_file}")
        print(f"📊 Statistics:")
        print(f"   - Total lines: {len(lines):,}")
        print(f"   - Total characters: {len(final_content):,}")
        print(f"   - File size: {len(final_content.encode('utf-8')):,} bytes")
        
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("\n🎉 Project overview v2.0 created successfully!")
    else:
        print("\n❌ Failed to create project overview.")