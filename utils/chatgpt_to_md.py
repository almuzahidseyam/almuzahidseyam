import json
import os
import re
from datetime import datetime

def sanitize_filename(title):
    # Remove invalid characters from filename
    title = re.sub(r'[\\/*?:"<>|]', "", title)
    return title.strip()[:100]  # Limit length

def convert_chatgpt_history(json_filepath, output_dir):
    """
    Reads the ChatGPT conversations.json file and exports each chat 
    into a beautiful Markdown file for offline reading.
    """
    if not os.path.exists(json_filepath):
        print(f"Error: Could not find {json_filepath}")
        print("Please extract your ChatGPT data export and place 'conversations.json' in this folder.")
        return

    os.makedirs(output_dir, exist_ok=True)
    
    with open(json_filepath, 'r', encoding='utf-8') as f:
        try:
            conversations = json.load(f)
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in conversations.json")
            return

    total_exported = 0

    for conv in conversations:
        title = conv.get('title', 'Untitled_Chat')
        safe_title = sanitize_filename(title)
        create_time = conv.get('create_time', 0)
        
        # Format date for the filename prefix (e.g., 2023-10-25_ChatTitle.md)
        if create_time:
            date_str = datetime.fromtimestamp(create_time).strftime('%Y-%m-%d')
            filename = f"{date_str}_{safe_title}.md"
        else:
            filename = f"UnknownDate_{safe_title}.md"
            
        filepath = os.path.join(output_dir, filename)
        
        # Extract messages
        mapping = conv.get('mapping', {})
        messages = []
        
        for node_id, node in mapping.items():
            msg = node.get('message')
            if not msg:
                continue
                
            author_role = msg.get('author', {}).get('role', 'unknown')
            content_parts = msg.get('content', {}).get('parts', [])
            
            # Combine content parts (usually just one text block)
            text_content = ""
            for part in content_parts:
                if isinstance(part, str):
                    text_content += part + "\n"
                    
            if text_content.strip():
                messages.append({
                    'role': author_role,
                    'text': text_content.strip(),
                    'create_time': msg.get('create_time', 0)
                })
                
        # Sort messages by time to ensure correct flow
        messages.sort(key=lambda x: x['create_time'] if x['create_time'] else 0)

        # Write to Markdown
        if messages:
            with open(filepath, 'w', encoding='utf-8') as md_file:
                md_file.write(f"# {title}\n")
                if create_time:
                    md_file.write(f"*Date: {datetime.fromtimestamp(create_time).strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
                md_file.write("---\n\n")
                
                for m in messages:
                    role = m['role'].capitalize()
                    text = m['text']
                    
                    if role == 'User':
                        md_file.write(f"**👤 You:**\n\n{text}\n\n")
                    elif role == 'Assistant':
                        md_file.write(f"**🤖 ChatGPT:**\n\n{text}\n\n")
                    elif role == 'System':
                        md_file.write(f"**⚙️ System:**\n\n_{text}_\n\n")
                
                # Appending user's copyright
                md_file.write("\n---\n*Exported via Custom Script*\nMuhammad Al-Muzahid | © 2026\n")
                
            total_exported += 1
            print(f"Exported: {filename}")

    print(f"\n✅ Successfully exported {total_exported} chats to Markdown format in the '{output_dir}' folder!")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert ChatGPT conversations.json to Markdown")
    parser.add_argument("--input", default="conversations.json", help="Path to conversations.json")
    parser.add_argument("--output", default="ChatGPT_Markdown_Archive", help="Output directory")
    args = parser.parse_args()
    
    convert_chatgpt_history(args.input, args.output)
