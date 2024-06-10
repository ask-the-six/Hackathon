from dataclasses import dataclass, field
from typing import List, Optional
from dataclasses_json import dataclass_json
import json

@dataclass_json
@dataclass
class Investment:
  investment_id: str
  investment_type: str
  amount: float

@dataclass_json
@dataclass
class Account:
  account_id: str
  account_type: str
  balance: float

@dataclass_json
@dataclass
class Portfolio:
  portfolio_id: str
  investments: List[Investment]
  total_value: float

@dataclass_json
@dataclass
class AnnualReview:
  year: int
  review_notes: str
  performance: float

@dataclass_json
@dataclass
class PhoneCall:
  call_id: str
  duration: int
  notes: str

@dataclass_json
@dataclass
class Email:
  email_id: str
  subject: str
  content: str

@dataclass_json
@dataclass
class Meeting:
  meeting_id: str
  location: str
  attendees: List[str]
  agenda: str



@dataclass_json
@dataclass
class Banker:
  banker_id: str
  name: str

@dataclass_json
@dataclass
class Client:
  client_id: str
  name: str
  accounts: List[Account]
  portfolio: Optional[Portfolio] = None
  annual_reviews: List[AnnualReview] = field(default_factory=list)
  phone_calls: List[PhoneCall] = field(default_factory=list)
  emails: List[Email] = field(default_factory=list)
  meetings: List[Meeting] = field(default_factory=list)
  primary_banker_id: Optional[str] = None




