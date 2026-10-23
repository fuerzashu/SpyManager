"""Public profile URL templates used by SpyManager."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Site:
    name: str
    template: str
    category: str

SITES = [
    Site("GitHub", "https://github.com/{username}", "Development"),
    Site("GitLab", "https://gitlab.com/{username}", "Development"),
    Site("Codeberg", "https://codeberg.org/{username}", "Development"),
    Site("Bitbucket", "https://bitbucket.org/{username}/", "Development"),
    Site("Hugging Face", "https://huggingface.co/{username}", "AI / Development"),
    Site("PyPI", "https://pypi.org/user/{username}/", "Development"),
    Site("Reddit", "https://www.reddit.com/user/{username}/", "Community"),
    Site("Medium", "https://medium.com/@{username}", "Writing"),
    Site("Dev.to", "https://dev.to/{username}", "Development"),
    Site("Hashnode", "https://hashnode.com/@{username}", "Writing"),
    Site("Twitch", "https://www.twitch.tv/{username}", "Streaming"),
    Site("YouTube", "https://www.youtube.com/@{username}", "Video"),
    Site("GitBook", "https://{username}.gitbook.io/", "Writing"),
    Site("Keybase", "https://keybase.io/{username}", "Community"),
    Site("Mastodon.social", "https://mastodon.social/@{username}", "Social"),
    Site("Docker Hub", "https://hub.docker.com/u/{username}", "Development"),
    Site("Replit", "https://replit.com/@{username}", "Development"),
    Site("Kaggle", "https://www.kaggle.com/{username}", "Data / AI"),
    Site("Instructables", "https://www.instructables.com/member/{username}/", "Community"),
    Site("Scratch", "https://scratch.mit.edu/users/{username}/", "Community"),
]
