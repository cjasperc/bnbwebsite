import shutil, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

mapping = {
    # HOMEPAGE
    "hero-composite-decking.jpg":       "hero-decking.jpg",
    "service-composite-decking.jpg":    "composite-decking-norwich.jpg",
    "service-trex.jpg":                 "trex-decking-norwich.jpg",
    "service-garden-rooms.jpg":         "garden-office-norwich.jpg",
    "service-garden-gym.jpg":           "garden-gym-norfolk.jpg",
    "service-garden-bar.jpg":           "garden-bar-norwich.jpg",
    "service-fencing.jpg":              "composite-fencing-norwich.webp",
    "og-image.jpg":                     "hero-decking.jpg",
    "gallery-decking-1.jpg":            "hero-decking.jpg",
    "gallery-decking-2.jpg":            "composite-decking-norwich.jpg",
    "gallery-decking-3.jpg":            "trex-decking-norwich.jpg",
    "gallery-decking-4.jpg":            "garden-transformation-norwich.jpg",
    "gallery-decking-5.jpg":            "wheelchair-accessible-deck.jpg",
    "gallery-decking-6.jpg":            "trex-decking-installation.jpg",
    # COMPOSITE DECKING
    "overview-composite-decking.jpg":   "trex-decking-norwich.jpg",
    "related-trex-transcend.jpg":       "trex-decking-norwich.jpg",
    "related-trex-enhance.jpg":         "homepage-image-4.jpg",
    "related-trex-signature.jpg":       "composite-decking-norwich.jpg",
    "related-composite-decking.jpg":    "composite-decking-norwich.jpg",
    "related-fencing.jpg":              "composite-fencing-norwich.webp",
    "related-garden-rooms.jpg":         "garden-office-norwich.jpg",
    "related-pergolas.jpg":             "pergola-norwich.jpg",
    # TREX PRODUCTS HUB
    "hero-trex-range.jpg":              "trex-decking-norwich.jpg",
    "trex-transcend.jpg":               "trex-decking-norwich.jpg",
    "trex-signature.jpg":               "composite-decking-norwich.jpg",
    "trex-enhance.jpg":                 "homepage-image-4.jpg",
    "trex-transcend-thumb.jpg":         "trex-decking-norwich.jpg",
    "trex-signature-thumb.jpg":         "composite-decking-norwich.jpg",
    # TREX TRANSCEND
    "hero-trex-transcend.jpg":          "trex-decking-norwich.jpg",
    "overview-trex-transcend.jpg":      "hero-decking.jpg",
    "transcend-island-mist.jpg":        "hero-decking.jpg",
    "transcend-gravel-path.jpg":        "composite-decking-norwich.jpg",
    "transcend-spiced-rum.jpg":         "trex-decking-norwich.jpg",
    "transcend-tiki-torch.jpg":         "homepage-image-1.jpg",
    "transcend-havana-gold.jpg":        "homepage-image-2.jpg",
    "transcend-lava-rock.jpg":          "homepage-image-3.jpg",
    "transcend-rope-swing.jpg":         "homepage-image-4.jpg",
    "transcend-lineage-island-mist.jpg":"homepage-image-5.jpg",
    "gallery-transcend-1.jpg":          "hero-decking.jpg",
    "gallery-transcend-2.jpg":          "composite-decking-norwich.jpg",
    "gallery-transcend-3.jpg":          "trex-decking-norwich.jpg",
    "gallery-transcend-4.jpg":          "garden-transformation-norwich.jpg",
    "gallery-transcend-5.jpg":          "wheelchair-accessible-deck.jpg",
    "gallery-transcend-6.jpg":          "trex-decking-installation.jpg",
    # TREX SIGNATURE
    "hero-trex-signature.jpg":          "composite-decking-norwich.jpg",
    "overview-trex-signature.jpg":      "trex-decking-norwich.jpg",
    "signature-whidbey.jpg":            "trex-signature-whidbey-board.png",
    "signature-island-mist.jpg":        "hero-decking.jpg",
    "signature-gravel-path.jpg":        "composite-decking-norwich.jpg",
    "signature-spiced-rum.jpg":         "homepage-image-1.jpg",
    "gallery-signature-1.jpg":          "composite-decking-norwich.jpg",
    "gallery-signature-2.jpg":          "hero-decking.jpg",
    "gallery-signature-3.jpg":          "trex-decking-norwich.jpg",
    "gallery-signature-4.jpg":          "garden-transformation-norwich.jpg",
    "gallery-signature-5.jpg":          "wheelchair-accessible-deck.jpg",
    "gallery-signature-6.jpg":          "homepage-image-2.jpg",
    # TREX ENHANCE
    "trex-enhance-hero.jpg":            "homepage-image-4.jpg",
    "trex-enhance-overview.jpg":        "homepage-image-2.jpg",
    "enhance-clam-shell.jpg":           "homepage-image-1.jpg",
    "enhance-beach-dune.jpg":           "homepage-image-2.jpg",
    "enhance-rocky-harbor.jpg":         "homepage-image-3.jpg",
    "enhance-toasted-sand.jpg":         "homepage-image-4.jpg",
    "enhance-foggy-wharf.jpg":          "homepage-image-5.jpg",
    "enhance-coastal-bluff.jpg":        "trex-decking-norwich.jpg",
    "enhance-gallery-1.jpg":            "homepage-image-1.jpg",
    "enhance-gallery-2.jpg":            "homepage-image-2.jpg",
    "enhance-gallery-3.jpg":            "homepage-image-3.jpg",
    "enhance-gallery-4.jpg":            "homepage-image-4.jpg",
    "enhance-gallery-5.jpg":            "homepage-image-5.jpg",
    # GARDEN ROOMS HUB
    "garden-rooms-hero.jpg":            "garden-office-norwich.jpg",
    "garden-rooms-overview.jpg":        "insulated-garden-room-hero.jpg",
    "garden-rooms-gallery-4.jpg":       "garden-rooms-gallery-1.jpg",
    "garden-rooms-gallery-5.jpg":       "garden-rooms-gallery-2.jpg",
    "garden-rooms-thumb.jpg":           "garden-room-exterior.jpg",
    "insulated-garden-rooms-thumb.jpg": "insulated-garden-room-hero.jpg",
    "garden-gyms-thumb.jpg":            "garden-gym-norfolk.jpg",
    "garden-bars-thumb.jpg":            "garden-bar-norwich.jpg",
    # INSULATED ROOMS
    "insulated-garden-rooms-hero.jpg":  "insulated-garden-room-hero.jpg",
    "insulated-garden-rooms-overview.jpg": "garden-office-norwich.jpg",
    "insulated-rooms-gallery-1.jpg":    "garden-office-norwich.jpg",
    "insulated-rooms-gallery-2.jpg":    "insulated-garden-room-hero.jpg",
    "insulated-rooms-gallery-3.jpg":    "garden-rooms-gallery-1.jpg",
    "insulated-rooms-gallery-4.jpg":    "garden-rooms-gallery-2.jpg",
    "insulated-rooms-gallery-5.jpg":    "garden-rooms-gallery-3.jpg",
    # GARDEN GYMS
    "garden-gyms-hero.jpg":             "garden-gym-norfolk.jpg",
    "garden-gyms-overview.jpg":         "garden-gym-norfolk.jpg",
    "gym-gallery-1.jpg":                "garden-gym-norfolk.jpg",
    "gym-gallery-2.jpg":                "homepage-image-3.jpg",
    "gym-gallery-3.jpg":                "homepage-image-5.jpg",
    "gym-gallery-4.jpg":                "garden-rooms-gallery-1.jpg",
    "gym-gallery-5.jpg":                "garden-rooms-gallery-2.jpg",
    # GARDEN BARS
    "garden-bars-hero.jpg":             "garden-bar-norwich.jpg",
    "garden-bars-overview.jpg":         "garden-bar-norwich.jpg",
    "bar-gallery-1.jpg":                "garden-bar-norwich.jpg",
    "bar-gallery-2.jpg":                "homepage-image-1.jpg",
    "bar-gallery-3.jpg":                "homepage-image-2.jpg",
    "bar-gallery-4.jpg":                "garden-rooms-gallery-3.jpg",
    "bar-gallery-5.jpg":                "garden-rooms-gallery-1.jpg",
    # PERGOLAS
    "pergolas-hero.jpg":                "pergola-norwich.jpg",
    "pergolas-overview.jpg":            "pergola-norwich.jpg",
    "pergola-open-beam.jpg":            "garden-transformation-norwich.jpg",
    "pergola-solid-roof.jpg":           "homepage-image-3.jpg",
    "pergola-louvred.jpg":              "homepage-image-5.jpg",
    "pergola-gallery-1.jpg":            "pergola-norwich.jpg",
    "pergola-gallery-2.jpg":            "garden-transformation-norwich.jpg",
    "pergola-gallery-3.jpg":            "homepage-image-3.jpg",
    "pergola-gallery-4.jpg":            "homepage-image-5.jpg",
    "pergola-gallery-5.jpg":            "garden-rooms-gallery-2.jpg",
    "pergolas-thumb.jpg":               "pergola-norwich.jpg",
    # FENCING
    "fencing-hero.jpg":                 "composite-fencing-norwich.webp",
    "fencing-overview.jpg":             "composite-fencing-norwich.webp",
    "fencing-gallery-1.jpg":            "composite-fencing-norwich.webp",
    "fencing-gallery-2.jpg":            "homepage-image-2.jpg",
    "fencing-gallery-3.jpg":            "homepage-image-3.jpg",
    "fencing-gallery-4.jpg":            "homepage-image-4.jpg",
    "fencing-gallery-5.jpg":            "homepage-image-5.jpg",
    "fencing-thumb.jpg":                "composite-fencing-norwich.webp",
    # GALLERY PAGE
    "gallery-deck-1.jpg":               "hero-decking.jpg",
    "gallery-deck-2.jpg":               "composite-decking-norwich.jpg",
    "gallery-deck-3.jpg":               "trex-decking-norwich.jpg",
    "gallery-deck-4.jpg":               "trex-decking-installation.jpg",
    "gallery-deck-5.jpg":               "wheelchair-accessible-deck.jpg",
    "gallery-room-1.jpg":               "garden-office-norwich.jpg",
    "gallery-room-2.jpg":               "insulated-garden-room-hero.jpg",
    "gallery-room-3.jpg":               "garden-rooms-gallery-3.jpg",
    "gallery-bar-1.jpg":                "garden-bar-norwich.jpg",
    "gallery-bar-2.jpg":                "garden-rooms-gallery-1.jpg",
    "gallery-gym-1.jpg":                "garden-gym-norfolk.jpg",
    "gallery-gym-2.jpg":                "garden-rooms-gallery-2.jpg",
    "gallery-pergola-1.jpg":            "pergola-norwich.jpg",
    "gallery-pergola-2.jpg":            "garden-transformation-norwich.jpg",
    "gallery-fence-1.jpg":              "composite-fencing-norwich.webp",
    "gallery-fence-2.jpg":              "homepage-image-2.jpg",
    # BLOG
    "blog-composite-vs-timber.jpg":     "composite-vs-timber-comparison.png",
    "blog-cost-guide.jpg":              "trex-decking-norwich.jpg",
    "blog-trex-colours.jpg":            "garden-transformation-norwich.jpg",
    "blog-planning.jpg":                "garden-office-norwich.jpg",
    "blog-maintenance.jpg":             "composite-decking-norwich.jpg",
    "blog-gym-guide.jpg":               "garden-gym-norfolk.jpg",
    "blog-pergola-types.jpg":           "pergola-norwich.jpg",
    "blog-trexpro.jpg":                 "trexpro-platinum-badge.png",
    "blog-accessible-garden.jpg":       "wheelchair-accessible-deck.jpg",
    "blog-jjh-install.jpg":             "trex-decking-installation.jpg",
    # THUMBNAILS
    "composite-decking-thumb.jpg":      "hero-decking.jpg",
}

created = 0
skipped = 0
missing = []

for target, source in mapping.items():
    if os.path.exists(target):
        skipped += 1
        continue
    if os.path.exists(source):
        shutil.copy2(source, target)
        created += 1
    else:
        missing.append(source + " -> " + target)

print("Created:", created)
print("Skipped:", skipped)
if missing:
    print("Missing sources:")
    for m in missing:
        print(" ", m)
else:
    print("All sources found - done.")
