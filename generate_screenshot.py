from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720

img = Image.new('RGB', (W, H), color='#1d2327')
draw = ImageDraw.Draw(img)

# Top bar
draw.rectangle([0, 0, W, 64], fill='#ff9900')

try:
    font_title = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 30)
    font_label = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 18)
    font_small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14)
    font_code  = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 13)
except Exception:
    font_title = font_label = font_small = font_code = ImageFont.load_default()

draw.text((24, 16), 'AWS SDK for PHP - WordPress Plugin', font=font_title, fill='#1d2327')

# Stat cards
cards = [
    ('SDK VERSION', '3.373.8'),
    ('RELEASE DATE', '2026-03-23'),
    ('AUTOLOADER', 'Active'),
]
card_x = 24
for label, value in cards:
    draw.rounded_rectangle([card_x, 90, card_x + 260, 190], radius=8, fill='#2c3338', outline='#3c434a')
    draw.text((card_x + 16, 102), label, font=font_small, fill='#8c8f94')
    col = '#00a32a' if value == 'Active' else '#f0f0f1'
    draw.text((card_x + 16, 130), value, font=font_label, fill=col)
    card_x += 280

# AWS service tiles
services = [
    ('EC2',          '#ff9900', 'Elastic Compute'),
    ('S3',           '#569a31', 'Simple Storage'),
    ('CloudFront',   '#8c4fff', 'CDN / Delivery'),
    ('Lambda',       '#e67e22', 'Serverless'),
    ('DynamoDB',     '#3f88c5', 'NoSQL Database'),
    ('SES',          '#d63638', 'Email Service'),
    ('SQS',          '#00b9e4', 'Queue Service'),
    ('Rekognition',  '#c0392b', 'Image Analysis'),
]

tile_w, tile_h = 136, 100
cols = 4
start_x, start_y = 24, 220
for i, (name, color, desc) in enumerate(services):
    col_i = i % cols
    row_i = i // cols
    x = start_x + col_i * (tile_w + 16)
    y = start_y + row_i * (tile_h + 12)
    draw.rounded_rectangle([x, y, x + tile_w, y + tile_h], radius=8, fill='#2c3338', outline=color)
    draw.rounded_rectangle([x, y, x + tile_w, y + 6], radius=4, fill=color)
    draw.text((x + 10, y + 18), name, font=font_label, fill=color)
    draw.text((x + 10, y + 58), desc, font=font_small, fill='#8c8f94')

# Code panel
panel_x = start_x + cols * (tile_w + 16) + 8
panel_y = 220
panel_w = W - panel_x - 24
panel_h = 240
draw.rounded_rectangle(
    [panel_x, panel_y, panel_x + panel_w, panel_y + panel_h],
    radius=8, fill='#0d1117', outline='#30363d'
)
draw.text((panel_x + 14, panel_y + 12), 'Usage Example', font=font_small, fill='#8c8f94')

code_lines = [
    ("if ( defined( 'AWS_SDK_WP_VERSION' ) ) {", '#ff7b72'),
    ("",                                          '#e6edf3'),
    ("    $s3 = new Aws\\S3\\S3Client([",         '#79c0ff'),
    ("        'region'  => 'us-east-1',",         '#a5d6ff'),
    ("        'version' => 'latest',",            '#a5d6ff'),
    ("    ]);",                                    '#e6edf3'),
    ("",                                          '#e6edf3'),
    ("    $cf = new Aws\\CloudFront\\CloudFrontClient([", '#79c0ff'),
    ("        'region'  => 'us-east-1',",         '#a5d6ff'),
    ("        'version' => 'latest',",            '#a5d6ff'),
    ("    ]);",                                    '#e6edf3'),
    ("}",                                         '#ff7b72'),
]

line_y = panel_y + 38
for line, col in code_lines:
    draw.text((panel_x + 14, line_y), line, font=font_code, fill=col)
    line_y += 16

# Footer
draw.rectangle([0, H - 40, W, H], fill='#2c3338')
draw.text((24, H - 28), 'Tools -> AWS SDK  |  mandato-wordpress/aws-sdk', font=font_small, fill='#8c8f94')
draw.text((W - 370, H - 28), 'github.com/mandato-wordpress/aws-sdk', font=font_small, fill='#8c8f94')

img.save('/home/user/aws-sdk/screenshot-1.png')
print('Done')
