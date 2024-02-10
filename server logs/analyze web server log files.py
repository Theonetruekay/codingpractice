import re
from collections import Counter

# Function to parse a single log entry
def parse_log_entry(log_entry):
    pattern = r'\[(.*?)\] (\w+) (\S+) (\d+) "(.*?)"'
    match = re.match(pattern, log_entry)
    if match:
        timestamp = match.group(1)
        http_method = match.group(2)
        url = match.group(3)
        status_code = match.group(4)
        user_agent = match.group(5)
        return timestamp, http_method, url, status_code, user_agent
    else:
        return None

# Function to analyze log file and calculate metrics
def analyze_log_file(log_file_path):
    total_requests = 0
    http_methods = []
    urls = []
    user_agents = []
    status_codes = []

    with open(log_file_path, 'r') as file:
        for line in file:
            log_entry = line.strip()
            parsed_entry = parse_log_entry(log_entry)
            if parsed_entry:
                total_requests += 1
                _, http_method, url, status_code, user_agent = parsed_entry
                http_methods.append(http_method)
                urls.append(url)
                status_codes.append(status_code)
                user_agents.append(user_agent)

    # Calculate metrics
    method_distribution = Counter(http_methods)
    top_urls = Counter(urls).most_common(5)
    top_user_agents = Counter(user_agents).most_common(5)
    status_code_frequency = Counter(status_codes)

    return {
        "Total Requests": total_requests,
        "HTTP Method Distribution": method_distribution,
        "Top URLs": top_urls,
        "Top User Agents": top_user_agents,
        "Status Code Frequency": status_code_frequency
    }

# Main function to execute the analysis
def main():
    log_file_path = "access.log"  # Path to the log file
    analysis_results = analyze_log_file(log_file_path)

    # Print analysis results
    print("Analysis Results:")
    print("Total Requests:", analysis_results["Total Requests"])
    print("HTTP Method Distribution:", analysis_results["HTTP Method Distribution"])
    print("Top URLs:", analysis_results["Top URLs"])
    print("Top User Agents:", analysis_results["Top User Agents"])
    print("Status Code Frequency:", analysis_results["Status Code Frequency"])

if __name__ == "__main__":
    main()
