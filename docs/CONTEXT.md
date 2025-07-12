# AlphaDataOmega Context & Assumptions

**Last Updated:** 2025-07-12

## Project Summary
AlphaDataOmega (ADO) is a sovereign blockchain lattice that creates AI-data harmony through decentralized content economy. The system features TRN as the flagship platform enabling creators to monetize content while maintaining data sovereignty through bounded AI agents and immutable storage.

## The Why Behind the Project
Current centralized AI systems create data sovereignty erosion where users lose control over their data and value flows inefficiently. ADO solves this through an immutable, interconnected lattice where users retain absolute control while AI agents operate within bounded parameters, preventing emergence risks and ensuring transparent value distribution.

## The How Behind the Project
Hybrid architecture combining OP Stack L2 for fast settlements, IPFS/Arweave for decentralized storage, bounded AI agents with local Llama models, and economic incentives through TRN token pegged to real storage costs ($0.065 based on IPFS+CDN infrastructure). Multi-signature security with 5-of-7 shard authentication ensures robust governance.

## The What Behind the Project
- Sovereign blockchain lattice with TRN content economy platform
- Economic tokens: ADO (governance, free-floating), TRN (content economy at $0.065 USD peg)
- Smart contracts: MintThrottleController (15.4M TRN/day), PegMechanism (±2% tolerance)
- Multi-signature security with NFT-based role management
- Bounded AI agents preventing emergence risks with semantic search
- Decentralized storage integration (IPFS/Arweave) for eternal data preservation

## How to use the project
1. **Development Setup:** Initialize with `forge init`, configure Kurtosis OP Stack devnet
2. **Contract Deployment:** Deploy ADO/TRN tokens, throttle controllers, peg mechanisms
3. **Economic Configuration:** Set authorized minters, configure throttle limits and peg tolerance
4. **Storage Integration:** Connect IPFS nodes and AI embedding services for content processing
5. **Application Building:** Use sovereign data infrastructure for decentralized applications
6. **Testing:** Comprehensive test suite with 100% coverage, economic validation, and fuzz testing

## Project Design Features

### 🌐 **Core Architecture Overview**
AlphaDataOmega (ADO) is a sovereign blockchain lattice with TRN (ThisRightNow) as the flagship L3 content platform. The system uses post-quantum cryptography, homomorphic embeddings, and zero-knowledge proofs to enable privacy-preserving content monetization while maintaining regulatory compliance.

**Key Components:**
- **Base Layer:** OP Stack L2 with IPFS/Arweave storage integration
- **L3s:** Organization-specific chains (universities, corporations)
- **L4s:** Personal/individual use chains
- **Multi-Context Protocol (MCP):** Cross-chain communication system
- **8-Shard Sovereignty:** 5-of-7 user recovery + hidden Master override shard
- **Homomorphic Embeddings:** Post-quantum secure content analysis without data exposure

### 🎯 **TRN Platform Specifics**
**Economic Model:**
- **$TRN:** Utility token (NOT pegged to fixed $0.065, but benchmarked to 10x IPFS storage costs)
- **$BRN:** Burn reserve notes for content moderation (users never hold, internal only)
- **InvestorNFTs:** Fixed supply of 100, receive 33% of DAO profits, support 1-layer fractional ownership
- **MasterNFT:** Ultimate veto authority with post-use DAO ratification requirement

**Content Moderation (Bless/Burn System):**
- **15% Burn Threshold:** Soft suppress (hidden from feeds)
- **25% Burn Threshold:** Auto-flag for DAO review
- **Fixed Cost:** 1 TRN per burn action (anti-spam protection)
- **AI Verification:** SemanticTrustOracle using homomorphic embeddings

### 🎛️ **TRN Dial Interface System**
**Circular Navigation Design:**
- **Central Dial:** Main navigation hub with orbital user arrangement
- **User Connections:** Arranged by interaction frequency (50%), mutual connections (30%), AI suggestions (20%)
- **Live Features:** Real-time streaming, comment integration, anonymous/location modes
- **Mobile-First:** Dark theme optimized for mobile with haptic feedback

**Social Features:**
- **Re-TRNs:** Limited to 1 layer depth, 60/30/10 revenue split (original/re-TRN/DAO)
- **Boosts:** Creator pays 3x TRN upfront, 90% to viewers, 10% to DAO, no creator cut
- **Subscriptions:** Creator-set pricing with 1.2x-2.0x payment multipliers

### 🔐 **Security & Privacy Architecture**
**8-Shard Sovereignty System:**
- **7 User Shards:** Shamir's Secret Sharing (5-of-7 threshold, GF(2^256) field)
- **Hidden 8th Shard:** BLS multi-signature from MasterNFT/Council, HSM custody
- **Geographic Distribution:** 3-5 datacenters across jurisdictions
- **Rotation Protocol:** 6-month DAO-elected rotation with ZK-masked identity

**Zero-Knowledge Compliance:**
- **ZK Circuits:** Groth16 with 128-bit security, ~10k constraints for Travel Rule
- **Trusted Setup:** Powers of Tau ceremony with 100+ MPC participants
- **Upgrades:** PLONK universal SRS for regulation changes without re-setup
- **Mobile ZK:** StarkWare Cairo 2.0 for real-time proof generation on mobile devices

### 🌍 **Cross-Border Compliance System**
**Geographic Enforcement:**
- **IP Detection:** MaxMind (primary), IP2Location (fallback), IPinfo (redundancy)
- **VPN Resistance:** Pattern analysis for IP cycling, ZK location proofs
- **CountryNFTs:** Geo-verified NFTs required for content access
- **Payment Rules:** Pay if legal in viewer jurisdiction, withhold if banned in creator jurisdiction

**Regulatory Framework:**
- **Travel Rule Compliance:** 100% industry adoption by 2025, ZK selective disclosure
- **EU 2027 Adaptation:** Auto-migration to non-biometric mode for privacy coin ban
- **Time-Limited Access:** Regulatory disclosure with 24-hour expiration windows
- **Audit Trails:** Immutable on-chain logs with tamper-proof Merkle proofs

### 💰 **Economic System Details**
**Token Supply & Minting:**
- **Genesis Supply:** 100M TRN (40% DAO treasury, 33% InvestorNFTs, 20% community, 7% dev)
- **Minting Triggers:** Usage-based validation (oracle-confirmed views/boosts)
- **Daily Throttle:** 15.4M TRN maximum (~$1M USD at benchmark)
- **Circuit Breakers:** Pause on oracle failures, internal AMM fallback

**Revenue Distribution:**
- **Standard Views:** 90% creator, 10% DAO
- **Re-TRN Views:** 60% original creator, 30% re-TRN creator, 10% DAO
- **Boosted Content:** 90% viewer reward, 10% DAO (creator paid upfront)
- **Ad Watching:** 0.33 TRN per ad (full credit after 10+ seconds)

**Boost Economics:**
- **Cost Structure:** 3x TRN per targeted view (paid upfront by creator)
- **Escrow System:** Funds locked in smart contract, released per verified view
- **Refund Mechanism:** Pro-rated return of unused budget post-campaign
- **AI Re-targeting:** Free suggestions using remaining escrow budget

### 🤖 **AI & Homomorphic Systems**
**SemanticTrustOracle:**
- **Encryption Scheme:** CKKS homomorphic encryption (8192 polynomial degree)
- **Performance:** 200ms latency, 1k/s throughput on 2025 GPU hardware
- **Security:** Ring-LWE based, 128-bit post-quantum security
- **Training:** Federated learning on anonymized L3 data with differential privacy

**Anti-Gaming ML:**
- **Pattern Detection:** Session velocity, geographic spread, temporal entropy, device diversity
- **Thresholds:** 700 suspicion = flag, 900 = auto-ban, <5% false positive rate
- **Adversarial Protection:** Robust training with adversarial examples, quarterly audits
- **Features:** Views/hour >50 flagged, single IP clusters detected, <3 device diversity suspicious

### 📡 **Infrastructure & Performance**
**OP Stack L2 Configuration:**
- **Gas Limits:** 30M gas per block, custom $ADO gas token
- **Sequencer:** Decentralized with 3/5 consensus, <1min failover recovery
- **Fraud Proofs:** 7-day challenge window, optimistic rollup security
- **Withdrawal:** 7-day standard, 1-hour fast withdrawals via ZK proofs (v2)

**IPFS/Arweave Integration:**
- **Pinning Strategy:** 3-node redundancy (Pinata + Filecoin + local)
- **Retention:** 7-day automatic, extended on view activity
- **Failover:** Multi-gateway queries, auto-repin if <2 nodes available
- **Permanent Storage:** Arweave for viral content (~$0.0001/KB)

**Real-Time Performance:**
- **TPS Targets:** 10k+ raw throughput, 5k+ effective with ZK overhead
- **Latency:** <5s for view processing, <100ms for TRN Dial interactions
- **Uptime:** 99.99% target with multi-node redundancy
- **Mobile Optimization:** 20% duty cycle for ZK proofs, offline queuing

### 🎮 **User Experience & Onboarding**
**Onboarding Flow:**
- **Task-Based:** 4-5 mandatory steps (shard creation, profile, first post, wallet setup)
- **Gamification:** Shard forging presented as quest narrative
- **Incentives:** 1 TRN bonus on completion (no ad requirement)
- **Tutorial:** Diversified shard storage warnings and best practices

**TRN Dial Navigation:**
- **Orbital Algorithm:** 20-30 most relevant users shown (AI-ranked score >0.7)
- **Manual Organization:** Drag/drop to pin users in inner orbits
- **Infinite Scroll:** Full connection list with pagination for 100+ connections
- **Real-Time Updates:** WebSocket pub/sub every 5s, optimistic Redux updates

**Ad-Watching System:**
- **Credit Rate:** 0.33 TRN per ad (3 ads = 1 TRN for content viewing)
- **Skip Mechanics:** Full credit after 10+ seconds watched
- **Daily Limits:** Prevent gaming through reasonable viewing quotas
- **Integration:** Seamless with content discovery and boost funding

### 🏛️ **Governance & DAO Structure**
**Governance Hierarchy:**
1. **MasterNFT:** Ultimate veto power, requires post-use DAO ratification
2. **InvestorNFTs:** 33% profit sharing, major decision voting rights
3. **CreatorNFTs:** Content policy and platform governance participation
4. **UserNFTs:** Basic governance participation and proposal submission

**Decision Making:**
- **Proposal Types:** POLICY, ECONOMIC, TECHNICAL, EMERGENCY
- **Quorum Requirements:** Configurable at DAO genesis (e.g., 7/12 for critical decisions)
- **Voting Process:** Council → community vote → Master veto check
- **Appeal System:** Anonymized appeals with SHA + differential privacy

**Profit Distribution:**
- **InvestorNFT Share:** 33% of platform fees + treasury appreciation
- **Calculation Basis:** View fees, boost revenue, subscription income, ad revenue
- **Exclusions:** No trading speculation or token price appreciation
- **Distribution:** Automatic to wallet, inactive NFTs still receive payments

### 🔍 **Content Moderation & Trust**
**Bless/Burn Mechanics:**
- **Voting Cost:** Fixed 1 TRN per action (prevents spam campaigns)
- **Threshold Effects:** 15% = soft suppress, 25% = auto-flag for DAO review
- **Vote Decay:** Temporal weighting to prevent historical pile-ons
- **Appeal Process:** Anonymized submission through DAO with human review

**Trust Score Calculation:**
- **Homomorphic Processing:** Content analysis without exposing raw data
- **Semantic Analysis:** Meaning and context understanding via embeddings
- **Community Signals:** Bless/burn ratios, view engagement, creator reputation
- **ML Integration:** Pattern recognition for quality assessment

### 📱 **Mobile & Offline Capabilities**
**Mobile ZK Optimization:**
- **Battery Management:** Background service with 20% active duty cycle
- **iOS Integration:** Background App Refresh compatibility
- **Android Integration:** WorkManager for proof generation scheduling
- **Performance:** StarkWare Cairo 2.0 for real-time mobile proof generation

**Offline Functionality:**
- **Content Access:** Cached content with local embeddings
- **Action Queuing:** Store bless/burn actions, posts for later submission
- **State Management:** Local storage with sync on reconnection
- **Limitations:** No live streaming, payments, or oracle-dependent features

### 🌐 **Multi-Chain & L3/L4 Architecture**
**L3 Deployment Templates:**
- **Organization Chains:** University departments, corporate divisions
- **Governance Isolation:** Independent DAO structures per organization
- **Data Sovereignty:** Encrypted on-chain data, local processing
- **MCP Integration:** Cross-L3 communication with retry/fallback mechanisms

**L4 Personal Chains:**
- **Individual Sovereignty:** Personal data and AI agent boundaries
- **Agent Integration:** Bounded AI agents with capability restrictions
- **Privacy Controls:** User-controlled data sharing and processing limits
- **Interoperability:** Selective data sharing with L3 organizations

### 🔒 **Privacy & Data Protection**
**GDPR Compliance:**
- **Data Minimization:** Only necessary data collection and processing
- **Right to Export:** JSON format with hashes for cross-platform portability
- **Right to Deletion:** Off-chain data removal, on-chain flagging/pseudonymization
- **Consent Management:** Granular privacy controls via shard-based authorization

**Data Retention:**
- **On-Chain:** Immutable references and logs (eternal preservation)
- **Off-Chain:** 30-day retention for analytics, GDPR-compliant deletion
- **User Control:** Export tools for data sovereignty and platform migration
- **Encryption:** All personal data encrypted with user-controlled keys

## Project Assumptions:
- Project name: AlphaDataOmega (sovereign blockchain lattice for AI-data harmony)
- Primary language: Hybrid - Solidity (on-chain) + Python (off-chain services)
- Modular architecture with clear separation of concerns
- Focus: Sovereign blockchain lattice with TRN as flagship decentralized content platform
- Preference for well-structured, testable code with comprehensive documentation
- Target audience: Developers/businesses building decentralized apps, creators seeking sovereign AI tools
- Core problem: Data sovereignty erosion in centralized AI systems
- Timeline: Beta deployment Q1 2026 on OP Stack testnet
- Scale: TB initially scaling to PB via off-chain storage (IPFS/Arweave)
- Architecture: Hybrid OP Stack L2 + decentralized storage + bounded AI agents
- Key technologies: OP Stack, Solidity, React/Tailwind, IPFS/Arweave, Llama models
- Avoid: Centralized oracles, black-box ML, non-post-quantum crypto long-term
- Authentication: 5-of-7 shard-based auth with NFT-based roles
- MVP target: 10k+ DAU in TRN app, 50 test L3s via templates
- Development approach: UI prototypes first for UX validation, parallel with token contracts
- Local development: Kurtosis OP Stack devnet, Foundry with 100% test coverage
- Token mechanics: TRN peg ±2% variance, throttle logic, daily settlement batches
- Multi-signature: Custom 5-of-7 shard system using Threshold library (Shamir's)
- Storage implementation: Pinata/Infura for managed IPFS nodes, transition to local clusters
- AI models: Local Llama via Hugging Face, custom LangChain wrapper with bounds
- Vector database: Local FAISS for development, Weaviate for decentralized production
- Testing strategy: Foundry with cheatcodes, mock contracts, 100% coverage standard
- Development timeline: Week 1 foundation setup, token contracts, minimal UI prototype
- Project initialization: Standard `forge init` with OP Stack foundry.toml configuration
- Contract architecture: ADO (governance), TRN (content+peg), MintThrottleController, PegMechanism
- Token economics specifics: TRN ±2% peg tolerance, daily/per-tx throttle limits, eternal audit logs
- Testing approach: Foundry fuzz testing from Day 1, mock oracles, property-based testing
- Git workflow: Feature branches, conventional commits, squash merges, GitHub Actions CI/CD
- OP Stack setup: Kurtosis devnet with pre-funded account for development
- Day 1 targets: Complete token contracts, throttle controller, peg mechanism, 100% test coverage
- Economic validation: TRN peg research-validated at $0.065 (10x real storage costs)
- Real-world cost basis: 3-min video IPFS+CDN = $0.0065, TRN = $0.065 (sustainable)
- Refined throttle limits: 15.4M TRN/day (~$1M USD), 1.5M TRN/tx (~$100K USD)
- Peg target confirmed: USD via Chainlink primary, internal AMM fallback
- Access control: Authorized minters only (Oracle/vault contracts), no public minting
- Economic testing: Validate peg accuracy, real-world cost basis, throttle enforcement
- Implementation readiness: All prerequisites satisfied, ready for forge init execution
- Code templates: OpenZeppelin ERC20 base with custom controllers for throttling and peg
- Foundry best practices: Solidity ^0.8.20, proper remappings, comprehensive test structure
- Documentation structure: CONTEXT.md populated with project overview and usage guide
- Architecture design: Complete view tracking, Merkle settlement, and cross-border payment systems
- View validation: 10s+ watch time, engagement scoring, ML-powered anti-gaming detection
- Settlement optimization: 2048 creator batches, gas-efficient Merkle proofs, 5/7 oracle consensus
- Cross-border compliance: Geo-oracle jurisdiction routing, escrow for disputed payments
- Payment calculation: Dynamic pricing with engagement/quality/reputation multipliers
- Anti-gaming: ML pattern recognition, temporal analysis, device fingerprinting
- Economic sustainability: Automatic rate adjustment based on network metrics and TRN peg
- Implementation phases: 21-day rollout from core infrastructure to production hardening
- DISCUSSION_015 Technical Research: CKKS homomorphic encryption preferred for ML operations with precision loss tolerance
- Post-quantum libraries: Microsoft SEAL vs IBM HElib vs OpenFHE for homomorphic encryption implementation
- Shamir Secret Sharing: ERC-3450 standard exists for BIP-39 mnemonics, 8-shard implementation needs custom Solidity development
- Threshold signatures: Chainlink's Schnorr-like signatures cost 15k gas for verification in Solidity
- BGV scheme efficiency: More complex but optimal for batch operations on multiple ciphertexts
- RLWE security foundation: Ring-Learning With Errors problem provides quantum-resistant security for lattice crypto
- Hardware acceleration: GPU implementations available for BGV, BFV, CKKS schemes in 2025
- L3/L4 architecture gaps: MCP message routing and state synchronization protocols need technical specification
- TRN Dial performance: Orbital rendering algorithms and real-time content streaming through IPFS need optimization
- DISCUSSION_016 Integration Research: FHE market growing to $600B+ (2025), MKHE enables multi-party economic calculations
- Privacy-Compliance Paradox: Homomorphic encryption conflicts with KYC/Travel Rule transparency requirements
- RegTech 2025 trends: "Compliance as code" with automated wallet clustering and IP pattern analysis for VPN detection
- Cross-border challenges: Regulatory fragmentation, varied Travel Rule enforcement, geo-masking detection difficulties
- Technical priorities shifted: Privacy-compliance bridge must be solved before economic features in Phase 0
- Multi-Key Homomorphic Encryption: Enables encrypted revenue splits (60/30/10) with clustering optimization reducing compute 60%
- VPN detection methods: IP cycling pattern analysis effective but users can bypass with address rotation
- Zero-knowledge solutions needed: Location proofs and selective disclosure for regulatory compliance without privacy loss
- DISCUSSION_017 Privacy Solution: ZK proofs validated for regulatory acceptance, 100% Travel Rule compliance by 2025
- Production ZK systems: ZKsync, Polygon zkEVM with $312M+ TVL proving commercial viability of selective disclosure
- Mobile ZK proofs: StarkWare S-two enables real-time ZK generation on mobile devices for TRN Dial
- Geography-based privacy: EU 2027 ban driving compliant innovation, privacy fragmentation by jurisdiction
- Privacy-compliance bridge: VALIDATED as technically feasible using 2025 ZK selective disclosure architecture
- Conditional privacy: Privacy within regulatory boundaries becoming standard, satisfies compliance requirements
- ZK regulatory acceptance: Selective disclosure satisfies compliance without full transparency, industry adoption proven
- DISCUSSION_001 Market Research: StarkWare S-two enables mobile ZK proofs 39x faster than previous systems, production-ready Q4 2025
- Mobile ZK validation: Real-time proof generation on smartphones achieved, battery optimization through consumer-grade hardware approach
- Travel Rule 2025 status: Only 46% FATF countries fully implemented, ZK selective disclosure emerging as compliance bridge solution
- OP Stack L3 ecosystem: 40+ chains in Superchain, L3 support added with custom gas tokens and Plasma Mode for DA flexibility
- Regulatory positioning: "Selective transparency" language preferred over "privacy," compliance-first marketing enables broader adoption
- FATF updates June 2025: Standardized $1000 threshold, clarified payment chain responsibilities, enforcement remains inconsistent
- Infrastructure readiness: Multiple RaaS providers (Caldera, Conduit, Zeeve) support L3 deployment, 67.1% L2 market share validation
- DISCUSSION_002_UPDATED Two-Person Team: Serial development recommended over parallel for small teams (80% productivity loss from context switching)
- AI-augmented development: Claude Code provides 2-10x productivity gains, 79% automation rate vs 49% traditional coding
- Context Engineering effectiveness: Claude's 200K token window enables deep codebase understanding for complex projects
- Small team strategy: Focus single project MVP (TRN DApp) before ecosystem expansion, validation-driven progression essential
- Parallel workflow optimization: Human handles architecture/strategy while AI manages implementation, daily sync points critical
- Technology stack simplification: Start with proven standards, add bleeding-edge features in later phases for two-person viability
- DISCUSSION_003 MVP Research: OP Stack RaaS solutions (Zeeve, QuickNode) provide 60% cost reduction and 97% faster deployment for small teams
- Creator economy MVP benchmarks: Multi-revenue streams essential, AI-powered content tools standard, newsletter integration critical for 2025
- Minimum viable L2 requirements: Sequencer + Batcher + Proposer + Challenger services, Node.js v20, testnet-first approach
- Creator platform success factors: Platform diversification required (single platform = high risk), social commerce $82B+ market size
- MVP development reality: $20-150k budget range, user tolerance for compromise has decreased, delightful UX mandatory for traction
- Two-person blockchain deployment: RaaS automation tools essential, modular architecture prioritizes future scalability over complexity
- COMPREHENSIVE TECHNICAL SPECIFICATIONS (Final Implementation Ready):
- 8-Shard Security: Shamir SSS for 7 user shards (5-of-7 threshold, GF(2^256) PQ-compatible), hidden 8th via BLS multi-sig
- ZK Circuit Implementation: Groth16 with 128-bit security, ~10k constraints for Travel Rule, 150-250k gas on OP L2
- Powers of Tau ceremony: 100+ participants MPC setup, PLONK for upgrades (universal SRS, no re-setup)
- TRN Token Economics: 100M genesis supply, usage-based minting (15.4M daily cap), multi-oracle consensus required
- Boost Escrow System: 3x TRN upfront lock, pro-rated refunds, AI re-targeting covered by original budget
- Revenue Split Architecture: ReTRNSplitter contract, 60/30/10 splits, assembly optimization, rounding to DAO
- Geo-Blocking Stack: MaxMind/IP2Location/IPinfo APIs, Chainlink consensus, CountryNFT access control
- Homomorphic Embeddings: CKKS scheme (8192 polynomial degree), 200ms latency, 1k/s throughput on GPU
- Anti-Gaming ML: Session velocity/geo spread detection, <5% false positive rate, quarterly adversarial training
- TRN Dial Performance: WebSocket pub/sub, WebRTC fallback, Redux optimistic updates, <100ms latency
- Mobile ZK Optimization: 20% duty cycle background service, offline queuing, battery-aware proof generation
- IPFS/Arweave Strategy: 3-node redundancy, 7-day pinning, multi-gateway failover, permanent Arweave storage
- OP Stack Configuration: 30M gas/block, 7-day fraud proofs, decentralized sequencer fallback, <1min recovery
- Regulatory Compliance: Time-limited ZK disclosure, GDPR-compliant deletion, audit trail immutability
- Performance Targets: 10k+ TPS (5k effective with ZK), 99.99% uptime, RTO <5min, RPO <1min
- HSM Security: Multi-datacenter geographic distribution, ZK-masked MasterNFT rotation every 6 months
- EU 2027 Compliance: Auto-migration to non-biometric mode, JSON export tools, jurisdiction blocking capability

## Technical Preferences:
- **Blockchain:** OP Stack L2, Solidity smart contracts, Hardhat/Foundry for testing
- **Backend:** Python with FastAPI for off-chain services
- **Frontend:** React with Tailwind CSS for web interfaces
- **Storage:** IPFS/Arweave for decentralized storage, no traditional databases
- **AI/ML:** Bounded agents with Llama models, embeddings for semantic search
- **Integration:** MCP bridges for external connections, Chainlink VRF for randomness
- **Authentication:** Multi-signature (5-of-7 shards), NFT-based role management
- **Data Processing:** Real-time for engagement, batch for settlements
- **Testing:** Pytest for Python, Hardhat/Foundry for contracts
- **Code Quality:** Black formatting, type hints, comprehensive documentation

## Development Guidelines:
- Never create files longer than 500 lines
- Organize code into feature-based modules
- Always create unit tests for new features
- Use virtual environment (venv_linux) for Python commands
- Follow PEP8 and Google-style docstrings

