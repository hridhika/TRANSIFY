# og/models.py

from django.db import models
from django.contrib.auth.models import User # Django's built-in User model

class UserProfile(models.Model):
    # One-to-one relationship with Django's built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Solana wallet address
    solana_wallet_address = models.CharField(max_length=64, unique=True, blank=True, null=True)

    # Points system
    current_points = models.IntegerField(default=0)
    total_tokens_minted = models.IntegerField(default=0)

    # Referral system
    referral_code = models.CharField(max_length=10, unique=True, blank=True, null=True)
    # Link to the user who referred this user
    referred_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='referred_users')

    def __str__(self):
        return self.user.username

# --- Future Models (for reference, will be added later) ---

# class Location(models.Model):
#     """Represents a public transport stop or vehicle with a QR code."""
#     name = models.CharField(max_length=255)
#     qr_code_identifier = models.CharField(max_length=255, unique=True, help_text="Unique ID embedded in the physical QR code.")
#     location_type = models.CharField(max_length=50, choices=[('bus_stop', 'Bus Stop'), ('metro_station', 'Metro Station'), ('vehicle', 'Vehicle')], default='bus_stop')
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
# class Scan(models.Model):
#     """Records a user's check-in or check-out scan."""
#     user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
#     scan_time = models.DateTimeField(auto_now_add=True)
#     scan_type = models.CharField(max_length=10, choices=[('check-in', 'Check-in'), ('check-out', 'Check-out')])
#     points_earned = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.user_profile.user.username} - {self.scan_type} at {self.scan_time.strftime('%Y-%m-%d %H:%M')}"
#
# class TokenMintingLog(models.Model):
#     """Logs the minting of Transify Tokens."""
#     user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     points_consumed = models.IntegerField()
#     tokens_minted = models.IntegerField()
#     transaction_signature = models.CharField(max_length=100, unique=True, null=True, blank=True, help_text="Solana transaction signature.")
#     status = models.CharField(max_length=20, default='pending', choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')])
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"Minted {self.tokens_minted} for {self.user_profile.user.username} - Status: {self.status}"