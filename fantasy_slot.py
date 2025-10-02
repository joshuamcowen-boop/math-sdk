from math_engine import GameConfig, simulate, Paytable, Symbol

# Define fantasy-themed symbols with payouts (for 3, 4, 5 matches)
symbols = [
    Symbol('DRAGON', [0, 0, 0, 10, 50], is_scatter=False),  # High-value
    Symbol('WIZARD', [0, 0, 0, 5, 20]),                     # Medium-value
    Symbol('SWORD', [0, 0, 0, 3, 10]),                     # Low-value
    Symbol('GEM', [0, 0, 0, 2, 5]),                        # Low-value
    Symbol('WILD', [0, 0, 0, 15, 100], is_wild=True),      # Substitutes for all except Scatter
]

# Define 20 paylines for 5x4 grid (indices 0-19: left-to-right, top-to-bottom)
paylines = [
    [0, 1, 2, 3, 4],   # Top row
    [5, 6, 7, 8, 9],   # Second row
    [10, 11, 12, 13, 14],  # Third row
    [15, 16, 17, 18, 19],  # Bottom row
    [0, 6, 12, 18, 4],  # Diagonal zigzag
    [5, 11, 17, 3, 9],  # Zigzag
    [10, 6, 2, 8, 14],  # W-pattern
    [15, 11, 7, 13, 19],  # M-pattern
    [0, 5, 10, 15, 19],  # Diagonal top-left to bottom-right
    [4, 9, 14, 19, 15],  # Diagonal top-right to bottom-left
    [2, 7, 12, 17, 2],   # V-pattern
    [3, 8, 13, 18, 3],   # Inverted V
    [1, 6, 11, 16, 1],   # Middle zigzag
    [0, 11, 2, 13, 4],   # Cross pattern
    [5, 16, 7, 18, 9],   # Cross pattern
    [10, 1, 12, 3, 14],  # Wave pattern
    [15, 6, 17, 8, 19],  # Wave pattern
    [0, 7, 14, 11, 4],   # Random zigzag
    [5, 12, 19, 6, 9],   # Random zigzag
    [10, 17, 4, 1, 14],  # Random zigzag
]

# Game configuration
config = GameConfig(
    reels=5,              # 5 reels
    rows=4,               # 4 rows
    lines=len(paylines),  # 20 paylines
    symbols=symbols,
    paytable=Paytable(paylines=paylines),
    bet_sizes=[1, 5, 10, 25, 50],  # Bet amounts in credits
    rtp_target=0.965      # Target RTP 96.5%
)

# Run simulation
if __name__ == "__main__":
    simulate(
        config=config,
        sims=10000,         # 10,000 spins for testing
        threads=4,          # Use 4 CPU threads
        mode='base',        # Base game mode (no bonus for simplicity)
        output='lookup_fantasy_slot.json.zst'  # Compressed lookup table
    )
