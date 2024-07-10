x = ({
   "data": {
     "propertySearch": {
       "__typename": "PropertySearchResults",
       "filterMetadata": {
         "__typename": "PropertyFilterMetadata",
         "amenities": [
           {
             "__typename": "PropertyAmenityValue",
             "id": 7
           },
           {
             "__typename": "PropertyAmenityValue",
             "id": 82
           },
           {
             "__typename": "PropertyAmenityValue",
             "id": 19
           },
           {
             "__typename": "PropertyAmenityValue",
             "id": 27
           },
           {
             "__typename": "PropertyAmenityValue",
             "id": 80
           },
           {
             "__typename": "PropertyAmenityValue",
             "id": 84
           },
           {
             "__typename": "PropertyAmenityValue",
             "id": 85
           }
         ],
         "neighborhoods": [
           {
             "__typename": "Neighborhood",
             "name": "London (and vicinity)",
             "regionId": "178279"
           },
           {
             "__typename": "Neighborhood",
             "name": "London City Centre",
             "regionId": "6195474"
           },
           {
             "__typename": "Neighborhood",
             "name": "Kings Cross St. Pancras",
             "regionId": "6047476"
           },
           {
             "__typename": "Neighborhood",
             "name": "Mayfair",
             "regionId": "6054503"
           },
           {
             "__typename": "Neighborhood",
             "name": "Canary Wharf",
             "regionId": "179523"
           },
           {
             "__typename": "Neighborhood",
             "name": "Kensington",
             "regionId": "6054501"
           },
           {
             "__typename": "Neighborhood",
             "name": "Notting Hill",
             "regionId": "601720"
           },
           {
             "__typename": "Neighborhood",
             "name": "Greenwich",
             "regionId": "5827"
           },
           {
             "__typename": "Neighborhood",
             "name": "Paddington",
             "regionId": "800049"
           },
           {
             "__typename": "Neighborhood",
             "name": "The City of London",
             "regionId": "800056"
           },
           {
             "__typename": "Neighborhood",
             "name": "Covent Garden",
             "regionId": "553248625846408347"
           },
           {
             "__typename": "Neighborhood",
             "name": "City of Westminster",
             "regionId": "179536"
           },
           {
             "__typename": "Neighborhood",
             "name": "Wimbledon",
             "regionId": "179539"
           },
           {
             "__typename": "Neighborhood",
             "name": "Victoria",
             "regionId": "800051"
           },
           {
             "__typename": "Neighborhood",
             "name": "Soho",
             "regionId": "6054504"
           },
           {
             "__typename": "Neighborhood",
             "name": "Stratford",
             "regionId": "6144705"
           },
           {
             "__typename": "Neighborhood",
             "name": "Chelsea",
             "regionId": "6054502"
           },
           {
             "__typename": "Neighborhood",
             "name": "Camden Town",
             "regionId": "179518"
           },
           {
             "__typename": "Neighborhood",
             "name": "London (LHR-Heathrow)",
             "regionId": "5392460"
           },
           {
             "__typename": "Neighborhood",
             "name": "London Paddington Station",
             "regionId": "6189104"
           }
         ],
         "priceRange": {
           "__typename": "PriceRange",
           "max": 1443.82,
           "min": 1443.82
         }
       },
       "universalSortAndFilter": {
         "__typename": "ShoppingSortAndFilters",
         "toolbar": {
           "__typename": "UIToolbar",
           "primary": "Sort & Filter",
           "actions": {
             "__typename": "UIToolbarActions",
             "primary": {
               "__typename": "UITertiaryButton",
               "primary": 'null',
               "action": {
                 "__typename": "ShoppingSortAndFilterAction",
                 "actionType": "CLOSE_AND_DO_NOT_APPLY",
                 "accessibility": 'null',
                 "analytics": {
                   "__typename": "ClientSideAnalytics",
                   "linkName": "close search filters dialog",
                   "referrerId": "HOT.SR.CloseFilterDialog.Close"
                 }
               }
             },
             "secondaries": [
               {
                 "__typename": "UITertiaryButton",
                 "primary": "Clear",
                 "disabled": 'false',
                 "action": {
                   "__typename": "ShoppingSortAndFilterAction",
                   "actionType": "CLEAR_DATA",
                   "accessibility": "All selections now cleared",
                   "analytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "clear all selections",
                     "referrerId": "HOT.SR.ClearFilters"
                   }
                 }
               }
             ]
           }
         },
         "revealAction": {
           "__typename": "UISecondaryFloatingActionButton",
           "primary": "Sort & Filter",
           "action": {
             "__typename": "ShoppingSortAndFilterAction",
             "actionType": "OPEN_MODAL",
             "accessibility": 'null',
             "analytics": {
               "__typename": "ClientSideAnalytics",
               "linkName": "Launch filters takeover",
               "referrerId": "HOT.SR:FilterControl"
             }
           },
           "accessibility": "1 filter applied. Change sort or apply more filters.",
           "badge": 1,
           "disabled": 'false',
           "icon": {
             "__typename": "Icon",
             "id": "tune",
             "description": "reveals sort and filter window",
             "size": 'null',
             "token": "icon__tune",
             "theme": 'null'
           }
         },
         "applyAction": {
           "__typename": "UIPrimaryFloatingActionButton",
           "primary": "Done",
           "action": {
             "__typename": "ShoppingSortAndFilterAction",
             "actionType": "CLOSE_AND_APPLY",
             "accessibility": 'null',
             "analytics": {
               "__typename": "ClientSideAnalytics",
               "linkName": "done search filters dialog",
               "referrerId": "HOT.SR.FilterControlDone"
             }
           },
           "accessibility": "Apply and close Sort and Filter",
           "badge": 'null',
           "disabled": 'false',
           "icon": 'null'
         },
         "filterSections": [
           {
             "__typename": "ShoppingSortAndFilterSection",
             "title": "Search by property name",
             "fields": [
               {
                 "__typename": "ShoppingTextInputField",
                 "primary": 'null',
                 "secondary": 'null',
                 "action": {
                   "__typename": "ShoppingSortAndFilterAction",
                   "actionType": "OPEN_MODAL",
                   "accessibility": 'null',
                   "analytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   }
                 },
                 "id": "hotelName",
                 "label": 'null',
                 "placeholder": "e.g. Marriott",
                 "selected": 'null',
                 "typeaheadInfo": {
                   "__typename": "TypeaheadInfo",
                   "client": "Hotels.Search",
                   "isDestination": 'true',
                   "lineOfBusiness": "hotels",
                   "maxNumberOfResults": 10,
                   "packageType": 'null',
                   "personalize": 'false',
                   "regionType": 128,
                   "typeaheadFeatures":
 "ta_hierarchy|postal_code|contextual_ta|consistent_display"
                 },
                 "icon": {
                   "__typename": "Icon",
                   "id": "search",
                   "description": "magnifying glass",
                   "size": 'null',
                   "token": "icon__search",
                   "theme": 'null'
                 },
                 "analytics": {
                   "__typename": "ClientSideAnalytics",
                   "linkName": "hotelName.",
                   "referrerId": "HOT.SR.hotelName."
                 }
               }
             ]
           },
           {
             "__typename": "ShoppingSortAndFilterSection",
             "title": "Filter by",
             "fields": [
               {
                 "__typename": "ShoppingMultiSelectionField",
                 "primary": "Popular filters",
                 "secondary": 'null',
                 "expando": {
                   "__typename": "ShoppingSelectionExpando",
                   "threshold": 5,
                   "collapseLabel": "See less",
                   "expandLabel": "See more",
                   "collapseAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   },
                   "expandAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   }
                 },
                 "multiSelectionOptions": [
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "lodging",
                     "primary": "Hotel",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "HOTEL",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "lodging.HOTEL",
                       "referrerId":
 "HOT.SR.popularFilter.lodging.HOTEL.'true':1"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "lodging.HOTEL",
                       "referrerId":
 "HOT.SR.popularFilter.lodging.HOTEL.'false':1"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "London City Centre",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "6195474",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.6195474",
                       "referrerId":
 "HOT.SR.popularFilter.regionId.6195474.'true':2"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.6195474",
                       "referrerId":
 "HOT.SR.popularFilter.regionId.6195474.'false':2"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "mealPlan",
                     "primary": "Breakfast included",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "FREE_BREAKFAST",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "mealPlan.FREE_BREAKFAST",
                       "referrerId":
 "HOT.SR.popularFilter.mealPlan.FREE_BREAKFAST.'true':3"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "mealPlan.FREE_BREAKFAST",
                       "referrerId":
 "HOT.SR.popularFilter.mealPlan.FREE_BREAKFAST.'false':3"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "paymentType",
                     "primary": "Fully refundable",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "FREE_CANCELLATION",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "paymentType.FREE_CANCELLATION",
                       "referrerId":
 "HOT.SR.popularFilter.paymentType.FREE_CANCELLATION.'true':4"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "paymentType.FREE_CANCELLATION",
                       "referrerId":
 "HOT.SR.popularFilter.paymentType.FREE_CANCELLATION.'false':4"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "Air conditioned",
                     "secondary": "",
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "AIR_CONDITIONING",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.AIR_CONDITIONING",
                       "referrerId":
 "HOT.SR.popularFilter.amenities.AIR_CONDITIONING.'true':5"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.AIR_CONDITIONING",
                       "referrerId":
 "HOT.SR.popularFilter.amenities.AIR_CONDITIONING.'false':5"
                     }
                   }
                 ]
               },
               {
                 "__typename": "ShoppingRangeField",
                 "primary": "Price per night",
                 "secondary": 'null',
                 "range": {
                   "__typename": "ShoppingRangeFilterOption",
                   "id": "price",
                   "primary": "",
                   "secondary": 'null',
                   "icon": 'null',
                   "analytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "price.",
                     "referrerId": "HOT.SR.price."
                   },
                   "selected": {
                     "__typename": "RangeValue",
                     "id": "price",
                     "min": 0,
                     "max": 300
                   },
                   "characteristics": {
                     "__typename": "ShoppingRangeCharacteristics",
                     "min": 0,
                     "max": 300,
                     "step": 30,
                     "labels": [
                       {
                         "__typename": "ShoppingRangeLabel",
                         "label": "$0",
                         "value": 0
                       },
                       {
                         "__typename": "ShoppingRangeLabel",
                         "label": "$30",
                         "value": 30
                       },
                       {
                         "__typename": "ShoppingRangeLabel",
                         "label": "$60",
                         "value": 60
                       },
                       {
                         "__typename": "ShoppingRangeLabel",
                         "label": "$90",
                         "value": 90
                       },
                       {
                         "__typename": "ShoppingRangeLabel",
                         "label": "$120",
                         "value": 120
                       },
                       {
                         "__typename": "ShoppingRangeLabel",
                         "label": "$150",
                         "value": 150
                       },
                       {
                         "__typename": "ShoppingRangeLabel",
                         "label": "$180",
                         "value": 180
                       },
                       {
                         "__typename": "ShoppingRangeLabel",
                         "label": "$210",
                         "value": 210
                       },
                       {
                         "__typename": "ShoppingRangeLabel",
                         "label": "$240",
                         "value": 240
                       },
                       {
                         "__typename": "ShoppingRangeLabel",
                         "label": "$270",
                         "value": 270
                       },
                       {
                         "__typename": "ShoppingRangeLabel",
                         "label": "$300+",
                         "value": 300
                       }
                     ]
                   }
                 }
               },
               {
                 "__typename": "ShoppingSelectionField",
                 "primary": "Guest rating",
                 "secondary": 'null',
                 "expando": {
                   "__typename": "ShoppingSelectionExpando",
                   "threshold": 5,
                   "collapseLabel": "See less",
                   "expandLabel": "See more",
                   "collapseAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   },
                   "expandAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   }
                 },
                 "options": [
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "guestRating",
                     "primary": "Any",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "",
                     "description": 'null',
                     "selected": 'true',
                     "disabled": 'false',
                     "default": 'true',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "guestRating.ANY",
                       "referrerId": "HOT.SR.guestRating.ANY.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "guestRating.ANY",
                       "referrerId": "HOT.SR.guestRating.ANY.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "guestRating",
                     "primary": "Wonderful 9+",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "45",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "guestRating.45",
                       "referrerId": "HOT.SR.guestRating.45.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "guestRating.45",
                       "referrerId": "HOT.SR.guestRating.45.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "guestRating",
                     "primary": "Very good 8+",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "40",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "guestRating.40",
                       "referrerId": "HOT.SR.guestRating.40.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "guestRating.40",
                       "referrerId": "HOT.SR.guestRating.40.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "guestRating",
                     "primary": "Good 7+",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "35",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "guestRating.35",
                       "referrerId": "HOT.SR.guestRating.35.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "guestRating.35",
                       "referrerId": "HOT.SR.guestRating.35.'false'"
                     }
                   }
                 ]
               },
               {
                 "__typename": "ShoppingMultiSelectionStackedTileField",
                 "primary": "Star rating",
                 "secondary": 'null',
                 "tileMultiSelectionOptions": [
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "star",
                     "primary": "1",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "star",
                       "description": "star",
                       "size": 'null',
                       "token": "icon__star",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "10",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "star.10",
                       "referrerId": "HOT.SR.star.10.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "star.10",
                       "referrerId": "HOT.SR.star.10.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "star",
                     "primary": "2",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "star",
                       "description": "star",
                       "size": 'null',
                       "token": "icon__star",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "20",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "star.20",
                       "referrerId": "HOT.SR.star.20.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "star.20",
                       "referrerId": "HOT.SR.star.20.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "star",
                     "primary": "3",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "star",
                       "description": "star",
                       "size": 'null',
                       "token": "icon__star",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "30",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "star.30",
                       "referrerId": "HOT.SR.star.30.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "star.30",
                       "referrerId": "HOT.SR.star.30.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "star",
                     "primary": "4",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "star",
                       "description": "star",
                       "size": 'null',
                       "token": "icon__star",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "40",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "star.40",
                       "referrerId": "HOT.SR.star.40.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "star.40",
                       "referrerId": "HOT.SR.star.40.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "star",
                     "primary": "5",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "star",
                       "description": "star",
                       "size": 'null',
                       "token": "icon__star",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "50",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "star.50",
                       "referrerId": "HOT.SR.star.50.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "star.50",
                       "referrerId": "HOT.SR.star.50.'false'"
                     }
                   }
                 ]
               },
               {
                 "__typename": "ShoppingMultiSelectionField",
                 "primary": "Payment type",
                 "secondary": 'null',
                 "expando": {
                   "__typename": "ShoppingSelectionExpando",
                   "threshold": 3,
                   "collapseLabel": "See less",
                   "expandLabel": "See more",
                   "collapseAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   },
                   "expandAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   }
                 },
                 "multiSelectionOptions": [
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "paymentType",
                     "primary": "Fully refundable",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "FREE_CANCELLATION",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "paymentType.FREE_CANCELLATION",
                       "referrerId":
 "HOT.SR.paymentType.FREE_CANCELLATION.'true':1"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "paymentType.FREE_CANCELLATION",
                       "referrerId":
 "HOT.SR.paymentType.FREE_CANCELLATION.'false':1"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "paymentType",
                     "primary": "Reserve now, pay later",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "PAY_LATER",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "paymentType.PAY_LATER",
                       "referrerId": "HOT.SR.paymentType.PAY_LATER.'true':2"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "paymentType.PAY_LATER",
                       "referrerId": "HOT.SR.paymentType.PAY_LATER.'false':2"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "paymentType",
                     "primary": "Pay with Hotels.com gift card",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "GIFT_CARD",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "paymentType.GIFT_CARD",
                       "referrerId": "HOT.SR.paymentType.GIFT_CARD.'true':3"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "paymentType.GIFT_CARD",
                       "referrerId": "HOT.SR.paymentType.GIFT_CARD.'false':3"
                     }
                   }
                 ]
               },
               {
                 "__typename": "ShoppingMultiSelectionField",
                 "primary": "Property type",
                 "secondary": 'null',
                 "expando": {
                   "__typename": "ShoppingSelectionExpando",
                   "threshold": 3,
                   "collapseLabel": "See less",
                   "expandLabel": "See more",
                   "collapseAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   },
                   "expandAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   }
                 },
                 "multiSelectionOptions": [
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "lodging",
                     "primary": "Hotel",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "HOTEL",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "lodging.HOTEL",
                       "referrerId": "HOT.SR.lodging.HOTEL.'true':1"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "lodging.HOTEL",
                       "referrerId": "HOT.SR.lodging.HOTEL.'false':1"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "lodging",
                     "primary": "Apart-hotel",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "APART_HOTEL",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "lodging.APART_HOTEL",
                       "referrerId": "HOT.SR.lodging.APART_HOTEL.'true':2"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "lodging.APART_HOTEL",
                       "referrerId": "HOT.SR.lodging.APART_HOTEL.'false':2"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "lodging",
                     "primary": "Apartment",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "APARTMENT",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "lodging.APARTMENT",
                       "referrerId": "HOT.SR.lodging.APARTMENT.'true':3"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "lodging.APARTMENT",
                       "referrerId": "HOT.SR.lodging.APARTMENT.'false':3"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "lodging",
                     "primary": "Bed & breakfast",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "BED_AND_BREAKFAST",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "lodging.BED_AND_BREAKFAST",
                       "referrerId":
 "HOT.SR.lodging.BED_AND_BREAKFAST.'true':4"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "lodging.BED_AND_BREAKFAST",
                       "referrerId":
 "HOT.SR.lodging.BED_AND_BREAKFAST.'false':4"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "lodging",
                     "primary": "House",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "VACATION_HOME",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "lodging.VACATION_HOME",
                       "referrerId": "HOT.SR.lodging.VACATION_HOME.'true':5"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "lodging.VACATION_HOME",
                       "referrerId": "HOT.SR.lodging.VACATION_HOME.'false':5"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "lodging",
                     "primary": "Villa",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "VILLA",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "lodging.VILLA",
                       "referrerId": "HOT.SR.lodging.VILLA.'true':6"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "lodging.VILLA",
                       "referrerId": "HOT.SR.lodging.VILLA.'false':6"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "lodging",
                     "primary": "Hotel resort",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "HOTEL_RESORT",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "lodging.HOTEL_RESORT",
                       "referrerId": "HOT.SR.lodging.HOTEL_RESORT.'true':7"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "lodging.HOTEL_RESORT",
                       "referrerId": "HOT.SR.lodging.HOTEL_RESORT.'false':7"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "lodging",
                     "primary": "Condo",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "CONDO",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "lodging.CONDO",
                       "referrerId": "HOT.SR.lodging.CONDO.'true':8"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "lodging.CONDO",
                       "referrerId": "HOT.SR.lodging.CONDO.'false':8"
                     }
                   }
                 ]
               },
               {
                 "__typename": "ShoppingMultiSelectionStackedTileField",
                 "primary": "Number of bedrooms",
                 "secondary": 'null',
                 "tileMultiSelectionOptions": [
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "bedroomFilter",
                     "primary": "Studio",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "0",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "bedroomFilter.0",
                       "referrerId": "HOT.SR.bedroomFilter.0.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "bedroomFilter.0",
                       "referrerId": "HOT.SR.bedroomFilter.0.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "bedroomFilter",
                     "primary": "1",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "1",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "bedroomFilter.1",
                       "referrerId": "HOT.SR.bedroomFilter.1.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "bedroomFilter.1",
                       "referrerId": "HOT.SR.bedroomFilter.1.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "bedroomFilter",
                     "primary": "2",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "2",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "bedroomFilter.2",
                       "referrerId": "HOT.SR.bedroomFilter.2.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "bedroomFilter.2",
                       "referrerId": "HOT.SR.bedroomFilter.2.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "bedroomFilter",
                     "primary": "3",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "3",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "bedroomFilter.3",
                       "referrerId": "HOT.SR.bedroomFilter.3.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "bedroomFilter.3",
                       "referrerId": "HOT.SR.bedroomFilter.3.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "bedroomFilter",
                     "primary": "4+",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "4",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "bedroomFilter.4",
                       "referrerId": "HOT.SR.bedroomFilter.4.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "bedroomFilter.4",
                       "referrerId": "HOT.SR.bedroomFilter.4.'false'"
                     }
                   }
                 ]
               },
               {
                 "__typename": "ShoppingSelectionField",
                 "primary": "Neighborhood",
                 "secondary": 'null',
                 "expando": {
                   "__typename": "ShoppingSelectionExpando",
                   "threshold": 3,
                   "collapseLabel": "See less",
                   "expandLabel": "See more",
                   "collapseAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   },
                   "expandAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   }
                 },
                 "options": [
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "London (and vicinity)",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "178279",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'true',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.178279",
                       "referrerId": "HOT.SR.regionId.178279.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.178279",
                       "referrerId": "HOT.SR.regionId.178279.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "London City Centre",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "6195474",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.6195474",
                       "referrerId": "HOT.SR.regionId.6195474.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.6195474",
                       "referrerId": "HOT.SR.regionId.6195474.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "London Paddington Station",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "6189104",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.6189104",
                       "referrerId": "HOT.SR.regionId.6189104.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.6189104",
                       "referrerId": "HOT.SR.regionId.6189104.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "Kensington",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "6054501",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.6054501",
                       "referrerId": "HOT.SR.regionId.6054501.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.6054501",
                       "referrerId": "HOT.SR.regionId.6054501.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "Covent Garden",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "553248625846408347",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.553248625846408347",
                       "referrerId":
 "HOT.SR.regionId.553248625846408347.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.553248625846408347",
                       "referrerId":
 "HOT.SR.regionId.553248625846408347.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "Mayfair",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "6054503",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.6054503",
                       "referrerId": "HOT.SR.regionId.6054503.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.6054503",
                       "referrerId": "HOT.SR.regionId.6054503.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "Camden Town",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "179518",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.179518",
                       "referrerId": "HOT.SR.regionId.179518.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.179518",
                       "referrerId": "HOT.SR.regionId.179518.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "City of Westminster",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "179536",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.179536",
                       "referrerId": "HOT.SR.regionId.179536.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.179536",
                       "referrerId": "HOT.SR.regionId.179536.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "Soho",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "6054504",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.6054504",
                       "referrerId": "HOT.SR.regionId.6054504.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.6054504",
                       "referrerId": "HOT.SR.regionId.6054504.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "The City of London",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "800056",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.800056",
                       "referrerId": "HOT.SR.regionId.800056.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.800056",
                       "referrerId": "HOT.SR.regionId.800056.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "Paddington",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "800049",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.800049",
                       "referrerId": "HOT.SR.regionId.800049.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.800049",
                       "referrerId": "HOT.SR.regionId.800049.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "Stratford",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "6144705",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.6144705",
                       "referrerId": "HOT.SR.regionId.6144705.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.6144705",
                       "referrerId": "HOT.SR.regionId.6144705.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "Chelsea",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "6054502",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.6054502",
                       "referrerId": "HOT.SR.regionId.6054502.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.6054502",
                       "referrerId": "HOT.SR.regionId.6054502.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "Notting Hill",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "601720",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.601720",
                       "referrerId": "HOT.SR.regionId.601720.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.601720",
                       "referrerId": "HOT.SR.regionId.601720.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "Kings Cross St. Pancras",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "6047476",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.6047476",
                       "referrerId": "HOT.SR.regionId.6047476.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.6047476",
                       "referrerId": "HOT.SR.regionId.6047476.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "Greenwich",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "5827",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.5827",
                       "referrerId": "HOT.SR.regionId.5827.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.5827",
                       "referrerId": "HOT.SR.regionId.5827.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "Canary Wharf",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "179523",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.179523",
                       "referrerId": "HOT.SR.regionId.179523.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.179523",
                       "referrerId": "HOT.SR.regionId.179523.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "Victoria",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "800051",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.800051",
                       "referrerId": "HOT.SR.regionId.800051.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.800051",
                       "referrerId": "HOT.SR.regionId.800051.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "Wimbledon",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "179539",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.179539",
                       "referrerId": "HOT.SR.regionId.179539.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.179539",
                       "referrerId": "HOT.SR.regionId.179539.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "regionId",
                     "primary": "London (LHR-Heathrow)",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "5392460",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.5392460",
                       "referrerId": "HOT.SR.regionId.5392460.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "regionId.5392460",
                       "referrerId": "HOT.SR.regionId.5392460.'false'"
                     }
                   }
                 ]
               },
               {
                 "__typename": "ShoppingSelectionField",
                 "primary": "Popular locations",
                 "secondary": 'null',
                 "expando": {
                   "__typename": "ShoppingSelectionExpando",
                   "threshold": 3,
                   "collapseLabel": "See less",
                   "expandLabel": "See more",
                   "collapseAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   },
                   "expandAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   }
                 },
                 "options": [
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "Any",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "",
                     "description": 'null',
                     "selected": 'true',
                     "disabled": 'false',
                     "default": 'true',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.ANY",
                       "referrerId": "HOT.SR.poi.ANY.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.ANY",
                       "referrerId": "HOT.SR.poi.ANY.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "Natural History Museum",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.496025,-0.176356:501537",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.496025,-0.176356:501537",
                       "referrerId":
 "HOT.SR.poi.51.496025,-0.176356:501537.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.496025,-0.176356:501537",
                       "referrerId":
 "HOT.SR.poi.51.496025,-0.176356:501537.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "Marble Arch",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.513207,-0.158882:508413",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.513207,-0.158882:508413",
                       "referrerId":
 "HOT.SR.poi.51.513207,-0.158882:508413.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.513207,-0.158882:508413",
                       "referrerId":
 "HOT.SR.poi.51.513207,-0.158882:508413.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "Hyde Park",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.507267,-0.16573:507738",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.507267,-0.16573:507738",
                       "referrerId":
 "HOT.SR.poi.51.507267,-0.16573:507738.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.507267,-0.16573:507738",
                       "referrerId":
 "HOT.SR.poi.51.507267,-0.16573:507738.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "The British Museum",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.518932,-0.126334:501529",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.518932,-0.126334:501529",
                       "referrerId":
 "HOT.SR.poi.51.518932,-0.126334:501529.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.518932,-0.126334:501529",
                       "referrerId":
 "HOT.SR.poi.51.518932,-0.126334:501529.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "London Bridge",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.50787,-0.08772:508412",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.50787,-0.08772:508412",
                       "referrerId":
 "HOT.SR.poi.51.50787,-0.08772:508412.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.50787,-0.08772:508412",
                       "referrerId":
 "HOT.SR.poi.51.50787,-0.08772:508412.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "Tower of London",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.508156,-0.076097:501521",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.508156,-0.076097:501521",
                       "referrerId":
 "HOT.SR.poi.51.508156,-0.076097:501521.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.508156,-0.076097:501521",
                       "referrerId":
 "HOT.SR.poi.51.508156,-0.076097:501521.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "Piccadilly Circus",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.509874,-0.13426:508415",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.509874,-0.13426:508415",
                       "referrerId":
 "HOT.SR.poi.51.509874,-0.13426:508415.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.509874,-0.13426:508415",
                       "referrerId":
 "HOT.SR.poi.51.509874,-0.13426:508415.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "Oxford Street",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.514823,-0.145919:6144897",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.514823,-0.145919:6144897",
                       "referrerId":
 "HOT.SR.poi.51.514823,-0.145919:6144897.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.514823,-0.145919:6144897",
                       "referrerId":
 "HOT.SR.poi.51.514823,-0.145919:6144897.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "Trafalgar Square",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.507988,-0.128025:508420",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.507988,-0.128025:508420",
                       "referrerId":
 "HOT.SR.poi.51.507988,-0.128025:508420.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.507988,-0.128025:508420",
                       "referrerId":
 "HOT.SR.poi.51.507988,-0.128025:508420.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "St. Paul\s Cathedral",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.513772,-0.099371:501558",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.513772,-0.099371:501558",
                       "referrerId":
 "HOT.SR.poi.51.513772,-0.099371:501558.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.513772,-0.099371:501558",
                       "referrerId":
 "HOT.SR.poi.51.513772,-0.099371:501558.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "Big Ben",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.500756,-0.124548:6060186",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.500756,-0.124548:6060186",
                       "referrerId":
 "HOT.SR.poi.51.500756,-0.124548:6060186.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.500756,-0.124548:6060186",
                       "referrerId":
 "HOT.SR.poi.51.500756,-0.124548:6060186.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "Westfield London Shopping Centre",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.507659,-0.221457:6159434",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.507659,-0.221457:6159434",
                       "referrerId":
 "HOT.SR.poi.51.507659,-0.221457:6159434.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.507659,-0.221457:6159434",
                       "referrerId":
 "HOT.SR.poi.51.507659,-0.221457:6159434.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "The Shard",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.5044,-0.086636:6273936",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.5044,-0.086636:6273936",
                       "referrerId":
 "HOT.SR.poi.51.5044,-0.086636:6273936.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.5044,-0.086636:6273936",
                       "referrerId":
 "HOT.SR.poi.51.5044,-0.086636:6273936.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "Buckingham Palace",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.501309,-0.141789:501516",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.501309,-0.141789:501516",
                       "referrerId":
 "HOT.SR.poi.51.501309,-0.141789:501516.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.501309,-0.141789:501516",
                       "referrerId":
 "HOT.SR.poi.51.501309,-0.141789:501516.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "London Eye",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.50339,-0.11956:6047451",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.50339,-0.11956:6047451",
                       "referrerId":
 "HOT.SR.poi.51.50339,-0.11956:6047451.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.50339,-0.11956:6047451",
                       "referrerId":
 "HOT.SR.poi.51.50339,-0.11956:6047451.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "ExCeL Exhibition Centre",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.508125,0.029794:6046590",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.508125,0.029794:6046590",
                       "referrerId":
 "HOT.SR.poi.51.508125,0.029794:6046590.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.508125,0.029794:6046590",
                       "referrerId":
 "HOT.SR.poi.51.508125,0.029794:6046590.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "Leicester Square",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.510412,-0.13009:508411",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.510412,-0.13009:508411",
                       "referrerId":
 "HOT.SR.poi.51.510412,-0.13009:508411.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.510412,-0.13009:508411",
                       "referrerId":
 "HOT.SR.poi.51.510412,-0.13009:508411.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "Tower Bridge",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.50561,-0.07523:508419",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.50561,-0.07523:508419",
                       "referrerId":
 "HOT.SR.poi.51.50561,-0.07523:508419.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.50561,-0.07523:508419",
                       "referrerId":
 "HOT.SR.poi.51.50561,-0.07523:508419.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "O2 Arena",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.502952,0.003227:6057080",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.502952,0.003227:6057080",
                       "referrerId":
 "HOT.SR.poi.51.502952,0.003227:6057080.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.502952,0.003227:6057080",
                       "referrerId":
 "HOT.SR.poi.51.502952,0.003227:6057080.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "poi",
                     "primary": "Wembley Stadium",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "51.556038,-0.2796:501565",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.556038,-0.2796:501565",
                       "referrerId":
 "HOT.SR.poi.51.556038,-0.2796:501565.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "poi.51.556038,-0.2796:501565",
                       "referrerId":
 "HOT.SR.poi.51.556038,-0.2796:501565.'false'"
                     }
                   }
                 ]
               },
               {
                 "__typename": "ShoppingMultiSelectionField",
                 "primary": "Meal plans available",
                 "secondary": 'null',
                 "expando": {
                   "__typename": "ShoppingSelectionExpando",
                   "threshold": 4,
                   "collapseLabel": "See less",
                   "expandLabel": "See more",
                   "collapseAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   },
                   "expandAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   }
                 },
                 "multiSelectionOptions": [
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "mealPlan",
                     "primary": "Breakfast included",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "FREE_BREAKFAST",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "mealPlan.FREE_BREAKFAST",
                       "referrerId": "HOT.SR.mealPlan.FREE_BREAKFAST.'true':1"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "mealPlan.FREE_BREAKFAST",
                       "referrerId":
 "HOT.SR.mealPlan.FREE_BREAKFAST.'false':1"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "mealPlan",
                     "primary": "Lunch included",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "HALF_BOARD",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "mealPlan.HALF_BOARD",
                       "referrerId": "HOT.SR.mealPlan.HALF_BOARD.'true':2"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "mealPlan.HALF_BOARD",
                       "referrerId": "HOT.SR.mealPlan.HALF_BOARD.'false':2"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "mealPlan",
                     "primary": "Dinner included",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "FULL_BOARD",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "mealPlan.FULL_BOARD",
                       "referrerId": "HOT.SR.mealPlan.FULL_BOARD.'true':3"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "mealPlan.FULL_BOARD",
                       "referrerId": "HOT.SR.mealPlan.FULL_BOARD.'false':3"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "mealPlan",
                     "primary": "All inclusive",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "ALL_INCLUSIVE",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "mealPlan.ALL_INCLUSIVE",
                       "referrerId": "HOT.SR.mealPlan.ALL_INCLUSIVE.'true':4"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "mealPlan.ALL_INCLUSIVE",
                       "referrerId": "HOT.SR.mealPlan.ALL_INCLUSIVE.'false':4"
                     }
                   }
                 ]
               },
               {
                 "__typename": "ShoppingMultiSelectionTileField",
                 "primary": "Amenities",
                 "secondary": 'null',
                 "tileMultiSelectionOptions": [
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "Air conditioned",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "ac_unit",
                       "description": "",
                       "size": 'null',
                       "token": "ac_unit",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "AIR_CONDITIONING",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.AIR_CONDITIONING",
                       "referrerId":
 "HOT.SR.amenities.AIR_CONDITIONING.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.AIR_CONDITIONING",
                       "referrerId":
 "HOT.SR.amenities.AIR_CONDITIONING.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "Pool",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "pool",
                       "description": "",
                       "size": 'null',
                       "token": "pool",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "POOL",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.POOL",
                       "referrerId": "HOT.SR.amenities.POOL.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.POOL",
                       "referrerId": "HOT.SR.amenities.POOL.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "WiFi included",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "wifi",
                       "description": "",
                       "size": 'null',
                       "token": "wifi",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "WIFI",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.WIFI",
                       "referrerId": "HOT.SR.amenities.WIFI.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.WIFI",
                       "referrerId": "HOT.SR.amenities.WIFI.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "Parking",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "local_parking",
                       "description": "",
                       "size": 'null',
                       "token": "local_parking",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "PARKING",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.PARKING",
                       "referrerId": "HOT.SR.amenities.PARKING.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.PARKING",
                       "referrerId": "HOT.SR.amenities.PARKING.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "Kitchen",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "kitchen",
                       "description": "",
                       "size": 'null',
                       "token": "kitchen",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "KITCHEN_KITCHENETTE",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.KITCHEN_KITCHENETTE",
                       "referrerId":
 "HOT.SR.amenities.KITCHEN_KITCHENETTE.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.KITCHEN_KITCHENETTE",
                       "referrerId":
 "HOT.SR.amenities.KITCHEN_KITCHENETTE.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "Gym",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "fitness_center",
                       "description": "",
                       "size": 'null',
                       "token": "fitness_center",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "GYM",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.GYM",
                       "referrerId": "HOT.SR.amenities.GYM.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.GYM",
                       "referrerId": "HOT.SR.amenities.GYM.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "Pet friendly",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "pets",
                       "description": "",
                       "size": 'null',
                       "token": "pets",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "PETS",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.PETS",
                       "referrerId": "HOT.SR.amenities.PETS.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.PETS",
                       "referrerId": "HOT.SR.amenities.PETS.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "Spa",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "spa",
                       "description": "",
                       "size": 'null',
                       "token": "spa",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "SPA_ON_SITE",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.SPA_ON_SITE",
                       "referrerId": "HOT.SR.amenities.SPA_ON_SITE.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.SPA_ON_SITE",
                       "referrerId": "HOT.SR.amenities.SPA_ON_SITE.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "Washer and dryer",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "local_laundry_service",
                       "description": "",
                       "size": 'null',
                       "token": "local_laundry_service",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "WASHER_DRYER",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.WASHER_DRYER",
                       "referrerId": "HOT.SR.amenities.WASHER_DRYER.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.WASHER_DRYER",
                       "referrerId": "HOT.SR.amenities.WASHER_DRYER.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "Outdoor space",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "balcony",
                       "description": "",
                       "size": 'null',
                       "token": "balcony",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "BALCONY_OR_TERRACE",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.BALCONY_OR_TERRACE",
                       "referrerId":
 "HOT.SR.amenities.BALCONY_OR_TERRACE.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.BALCONY_OR_TERRACE",
                       "referrerId":
 "HOT.SR.amenities.BALCONY_OR_TERRACE.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "Restaurant",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "local_dining",
                       "description": "",
                       "size": 'null',
                       "token": "local_dining",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "RESTAURANT_IN_HOTEL",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.RESTAURANT_IN_HOTEL",
                       "referrerId":
 "HOT.SR.amenities.RESTAURANT_IN_HOTEL.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.RESTAURANT_IN_HOTEL",
                       "referrerId":
 "HOT.SR.amenities.RESTAURANT_IN_HOTEL.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "Hot tub",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "hot_tub",
                       "description": "",
                       "size": 'null',
                       "token": "hot_tub",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "HOT_TUB",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.HOT_TUB",
                       "referrerId": "HOT.SR.amenities.HOT_TUB.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.HOT_TUB",
                       "referrerId": "HOT.SR.amenities.HOT_TUB.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "Cribs",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "bedding__crib",
                       "description": "",
                       "size": 'null',
                       "token": "bedding__crib",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "CRIB",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.CRIB",
                       "referrerId": "HOT.SR.amenities.CRIB.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.CRIB",
                       "referrerId": "HOT.SR.amenities.CRIB.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "Casino",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "casino",
                       "description": "",
                       "size": 'null',
                       "token": "casino",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "CASINO",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.CASINO",
                       "referrerId": "HOT.SR.amenities.CASINO.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.CASINO",
                       "referrerId": "HOT.SR.amenities.CASINO.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "Water park",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "water_park",
                       "description": "",
                       "size": 'null',
                       "token": "water_park",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "WATER_PARK",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.WATER_PARK",
                       "referrerId": "HOT.SR.amenities.WATER_PARK.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.WATER_PARK",
                       "referrerId": "HOT.SR.amenities.WATER_PARK.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "Ocean view",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "water",
                       "description": "",
                       "size": 'null',
                       "token": "water",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "OCEAN_VIEW",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.OCEAN_VIEW",
                       "referrerId": "HOT.SR.amenities.OCEAN_VIEW.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.OCEAN_VIEW",
                       "referrerId": "HOT.SR.amenities.OCEAN_VIEW.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "Electric car charging station",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "ev_station",
                       "description": "",
                       "size": 'null',
                       "token": "ev_station",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "ELECTRIC_CAR",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.ELECTRIC_CAR",
                       "referrerId": "HOT.SR.amenities.ELECTRIC_CAR.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.ELECTRIC_CAR",
                       "referrerId": "HOT.SR.amenities.ELECTRIC_CAR.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "amenities",
                     "primary": "Airport shuttle included",
                     "secondary": "",
                     "icon": {
                       "__typename": "Icon",
                       "id": "airport_shuttle",
                       "description": "",
                       "size": 'null',
                       "token": "airport_shuttle",
                       "theme": 'null'
                     },
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "FREE_AIRPORT_TRANSPORTATION",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.FREE_AIRPORT_TRANSPORTATION",
                       "referrerId":
 "HOT.SR.amenities.FREE_AIRPORT_TRANSPORTATION.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "amenities.FREE_AIRPORT_TRANSPORTATION",
                       "referrerId":
 "HOT.SR.amenities.FREE_AIRPORT_TRANSPORTATION.'false'"
                     }
                   }
                 ]
               },
               {
                 "__typename": "ShoppingMultiSelectionField",
                 "primary": "Hotels.com\\u00ae Rewards",
                 "secondary": 'null',
                 "expando": {
                   "__typename": "ShoppingSelectionExpando",
                   "threshold": 3,
                   "collapseLabel": "See less",
                   "expandLabel": "See more",
                   "collapseAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   },
                   "expandAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   }
                 },
                 "multiSelectionOptions": [
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "rewards",
                     "primary": "Redeem reward nights",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "REDEEM_REWARD_NIGHTS",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "rewards.REDEEM_REWARD_NIGHTS",
                       "referrerId":
 "HOT.SR.rewards.REDEEM_REWARD_NIGHTS.'true':1"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "rewards.REDEEM_REWARD_NIGHTS",
                       "referrerId":
 "HOT.SR.rewards.REDEEM_REWARD_NIGHTS.'false':1"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "rewards",
                     "primary": "VIP Access properties for superior stays",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "VIP",
                     "description": "Plus extra benefits for Silver and Gold members",
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "rewards.VIP",
                       "referrerId": "HOT.SR.rewards.VIP.'true':2"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "rewards.VIP",
                       "referrerId": "HOT.SR.rewards.VIP.'false':2"
                     }
                   }
                 ]
               },
               {
                 "__typename": "ShoppingMultiSelectionField",
                 "primary": "Accessibility",
                 "secondary": 'null',
                 "expando": {
                   "__typename": "ShoppingSelectionExpando",
                   "threshold": 3,
                   "collapseLabel": "See less",
                   "expandLabel": "See more",
                   "collapseAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   },
                   "expandAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   }
                 },
                 "multiSelectionOptions": [
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "accessibility",
                     "primary": "Elevator",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "ELEVATOR",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "accessibility.ELEVATOR",
                       "referrerId": "HOT.SR.accessibility.ELEVATOR.'true':1"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "accessibility.ELEVATOR",
                       "referrerId": "HOT.SR.accessibility.ELEVATOR.'false':1"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "accessibility",
                     "primary": "Accessible bathroom",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "ACCESSIBLE_BATHROOM",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "accessibility.ACCESSIBLE_BATHROOM",
                       "referrerId":
 "HOT.SR.accessibility.ACCESSIBLE_BATHROOM.'true':2"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "accessibility.ACCESSIBLE_BATHROOM",
                       "referrerId":
 "HOT.SR.accessibility.ACCESSIBLE_BATHROOM.'false':2"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "accessibility",
                     "primary": "In-room accessibility",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "IN_ROOM_ACCESSIBLE",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "accessibility.IN_ROOM_ACCESSIBLE",
                       "referrerId":
 "HOT.SR.accessibility.IN_ROOM_ACCESSIBLE.'true':3"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "accessibility.IN_ROOM_ACCESSIBLE",
                       "referrerId":
 "HOT.SR.accessibility.IN_ROOM_ACCESSIBLE.'false':3"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "accessibility",
                     "primary": "Roll-in shower",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "ROLL_IN_SHOWER",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "accessibility.ROLL_IN_SHOWER",
                       "referrerId":
 "HOT.SR.accessibility.ROLL_IN_SHOWER.'true':4"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "accessibility.ROLL_IN_SHOWER",
                       "referrerId":
 "HOT.SR.accessibility.ROLL_IN_SHOWER.'false':4"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "accessibility",
                     "primary": "Sign language-capable staff",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "SIGN_LANGUAGE_INTERPRETER",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName":
 "accessibility.SIGN_LANGUAGE_INTERPRETER",
                       "referrerId":
 "HOT.SR.accessibility.SIGN_LANGUAGE_INTERPRETER.'true':5"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName":
 "accessibility.SIGN_LANGUAGE_INTERPRETER",
                       "referrerId":
 "HOT.SR.accessibility.SIGN_LANGUAGE_INTERPRETER.'false':5"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "accessibility",
                     "primary": "Stair-free path to entrance",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "STAIR_FREE_PATH",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "accessibility.STAIR_FREE_PATH",
                       "referrerId":
 "HOT.SR.accessibility.STAIR_FREE_PATH.'true':6"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "accessibility.STAIR_FREE_PATH",
                       "referrerId":
 "HOT.SR.accessibility.STAIR_FREE_PATH.'false':6"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "accessibility",
                     "primary": "Wheelchair-accessible parking",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "ACCESSIBLE_PARKING",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "accessibility.ACCESSIBLE_PARKING",
                       "referrerId":
 "HOT.SR.accessibility.ACCESSIBLE_PARKING.'true':7"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "accessibility.ACCESSIBLE_PARKING",
                       "referrerId":
 "HOT.SR.accessibility.ACCESSIBLE_PARKING.'false':7"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "accessibility",
                     "primary": "Service animals allowed",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "SERVICE_ANIMAL",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "accessibility.SERVICE_ANIMAL",
                       "referrerId":
 "HOT.SR.accessibility.SERVICE_ANIMAL.'true':8"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "accessibility.SERVICE_ANIMAL",
                       "referrerId":
 "HOT.SR.accessibility.SERVICE_ANIMAL.'false':8"
                     }
                   }
                 ]
               },
               {
                 "__typename": "ShoppingMultiSelectionField",
                 "primary": "Traveler experience",
                 "secondary": 'null',
                 "expando": {
                   "__typename": "ShoppingSelectionExpando",
                   "threshold": 3,
                   "collapseLabel": "See less",
                   "expandLabel": "See more",
                   "collapseAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   },
                   "expandAnalytics": {
                     "__typename": "ClientSideAnalytics",
                     "linkName": "",
                     "referrerId": ""
                   }
                 },
                 "multiSelectionOptions": [
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "travelerType",
                     "primary": "LGBTQ welcoming",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "LGBT",
                     "description": "See properties that pledge to make all guests feel safe, welcome, and respected.",
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "travelerType.LGBT",
                       "referrerId": "HOT.SR.travelerType.LGBT.'true':1"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "travelerType.LGBT",
                       "referrerId": "HOT.SR.travelerType.LGBT.'false':1"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "travelerType",
                     "primary": "Business friendly",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "BUSINESS",
                     "description": "See properties with amenities to help you work comfortably, like WiFi and breakfast.",
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "travelerType.BUSINESS",
                       "referrerId": "HOT.SR.travelerType.BUSINESS.'true':2"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "travelerType.BUSINESS",
                       "referrerId": "HOT.SR.travelerType.BUSINESS.'false':2"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "travelerType",
                     "primary": "Family friendly",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "FAMILY",
                     "description": "See properties that include family essentials like in-room conveniences and activities for the kids.",
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "travelerType.FAMILY",
                       "referrerId": "HOT.SR.travelerType.FAMILY.'true':3"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "travelerType.FAMILY",
                       "referrerId": "HOT.SR.travelerType.FAMILY.'false':3"
                     }
                   }
                 ]
               },
               {
                 "__typename": "ShoppingMultiSelectionField",
                 "primary": "Availability",
                 "secondary": 'null',
                 "expando": 'null',
                 "multiSelectionOptions": [
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "availableFilter",
                     "primary": "Only show available properties",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "SHOW_AVAILABLE_ONLY",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "availableFilter.SHOW_AVAILABLE_ONLY",
                       "referrerId":
 "HOT.SR.availableFilter.SHOW_AVAILABLE_ONLY.'true':1"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "availableFilter.SHOW_AVAILABLE_ONLY",
                       "referrerId":
 "HOT.SR.availableFilter.SHOW_AVAILABLE_ONLY.'false':1"
                     }
                   }
                 ]
               }
             ]
           }
         ],
         "sortSections": [
           {
             "__typename": "ShoppingSortAndFilterSection",
             "title": 'null',
             "fields": [
               {
                 "__typename": "ShoppingDropdownField",
                 "primary": "Sort by",
                 "secondary": 'null',
                 "dropdownFilterOptions": [
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "sort",
                     "primary": "Recommended",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "RECOMMENDED",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'true',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "sort.RECOMMENDED",
                       "referrerId": "HOT.SR.sort.RECOMMENDED.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "sort.RECOMMENDED",
                       "referrerId": "HOT.SR.sort.RECOMMENDED.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "sort",
                     "primary": "Price: low to high",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "PRICE_LOW_TO_HIGH",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "sort.PRICE_LOW_TO_HIGH",
                       "referrerId": "HOT.SR.sort.PRICE_LOW_TO_HIGH.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "sort.PRICE_LOW_TO_HIGH",
                       "referrerId": "HOT.SR.sort.PRICE_LOW_TO_HIGH.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "sort",
                     "primary": "Price: high to low",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "PRICE_HIGH_TO_LOW",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "sort.PRICE_HIGH_TO_LOW",
                       "referrerId": "HOT.SR.sort.PRICE_HIGH_TO_LOW.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "sort.PRICE_HIGH_TO_LOW",
                       "referrerId": "HOT.SR.sort.PRICE_HIGH_TO_LOW.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "sort",
                     "primary": "Distance from downtown",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "DISTANCE",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "sort.DISTANCE",
                       "referrerId": "HOT.SR.sort.DISTANCE.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "sort.DISTANCE",
                       "referrerId": "HOT.SR.sort.DISTANCE.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "sort",
                     "primary": "Guest rating",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "REVIEW",
                     "description": 'null',
                     "selected": 'true',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "sort.REVIEW",
                       "referrerId": "HOT.SR.sort.REVIEW.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "sort.REVIEW",
                       "referrerId": "HOT.SR.sort.REVIEW.'false'"
                     }
                   },
                   {
                     "__typename": "ShoppingSelectableFilterOption",
                     "id": "sort",
                     "primary": "Star rating",
                     "secondary": 'null',
                     "icon": 'null',
                     "analytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "",
                       "referrerId": ""
                     },
                     "value": "PROPERTY_CLASS",
                     "description": 'null',
                     "selected": 'false',
                     "disabled": 'false',
                     "default": 'false',
                     "selectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "sort.PROPERTY_CLASS",
                       "referrerId": "HOT.SR.sort.PROPERTY_CLASS.'true'"
                     },
                     "deselectAnalytics": {
                       "__typename": "ClientSideAnalytics",
                       "linkName": "sort.PROPERTY_CLASS",
                       "referrerId": "HOT.SR.sort.PROPERTY_CLASS.'false'"
                     }
                   }
                 ]
               }
             ]
           }
         ]
       },
       "properties": [
         {
           "__typename": "Property",
           "id": "3849185",
           "featuredMessages": [],
           "name": "Corinthia London",
           "availability": {
             "__typename": "PropertyAvailability",
             "available": 'true',
             "minRoomsLeft": 3
           },
           "propertyImage": {
             "__typename": "PropertyImage",
             "alt": "",
             "fallbackImage": 'null',
             "image": {
               "__typename": "Image",
               "description": "Terrace/patio",
               "url":
 "https://images.trvl-media.com/lodging/4000000/3850000/3849200/3849185/70fa8edb.jpg?impolicy=resizecrop&rw=455&ra=fit"
             },
             "subjectId": 22007
           },
           "destinationInfo": {
             "__typename": "PropertyDestinationInfo",
             "distanceFromDestination": {
               "__typename": "Distance",
               "unit": "MILE",
               "value": 0.15
             },
             "distanceFromMessaging": 'null',
             "regionId": "2114"
           },
           "legalDisclaimer": 'null',
           "listingFooter": 'null',
           "mapMarker": {
             "__typename": "MapMarker",
             "label": "$1,444",
             "latLong": {
               "__typename": "Coordinates",
               "latitude": 51.50684,
               "longitude": -0.12435
             }
           },
           "neighborhood": {
             "__typename": "Region",
             "name": "City of Westminster"
           },
           "offerBadge": {
             "__typename": "OfferBadge",
             "primary": {
               "__typename": "Badge",
               "text": "VIP Access",
               "theme_temp": "VIP",
               "icon_temp": 'null',
               "mark": 'null'
             },
             "secondary": 'null'
           },
           "offerSummary": {
             "__typename": "OfferSummary",
             "messages": [
               {
                 "__typename": "OfferSummaryMessage",
                 "message": "Fully refundable",
                 "theme": "SUCCESS",
                 "type": "FREE_CANCEL",
                 "mark": 'null'
               },
               {
                 "__typename": "OfferSummaryMessage",
                 "message": "Reserve now, pay later",
                 "theme": "SUCCESS",
                 "type": "PAY_LATER",
                 "mark": 'null'
               },
               {
                 "__typename": "OfferSummaryMessage",
                 "message": "Collect stamps",
                 "theme": 'null',
                 "type": "LOYALTY_EARN",
                 "mark": {
                   "__typename": "Mark",
                   "id": "loyalty",
                   "token": "mark__loyalty",
                   "description": "loyalty logo"
                 }
               }
             ],
             "attributes": [
               {
                 "__typename": "OfferAttribute",
                 "type": "FREE_CANCELLATION"
               },
               {
                 "__typename": "OfferAttribute",
                 "type": "VIP"
               },
               {
                 "__typename": "OfferAttribute",
                 "type": "PAYMENT_CHOICE"
               }
             ]
           },
           "pinnedDetails": 'null',
           "price": {
             "__typename": "PropertyPrice",
             "options": [
               {
                 "__typename": "PropertyPriceOption",
                 "strikeOut": 'null',
                 "disclaimer": 'null',
                 "formattedDisplayPrice": "$1,444"
               }
             ],
             "priceMessaging": 'null',
             "lead": {
               "__typename": "Money",
               "amount": 1443.822857,
               "currencyInfo": {
                 "__typename": "Currency",
                 "code": "USD",
                 "symbol": "$"
               },
               "formatted": "$1,444"
             },
             "strikeOut": 'null',
             "displayMessages": [
               {
                 "__typename": "PriceDisplayMessage",
                 "lineItems": [
                   {
                     "__typename": "DisplayPrice",
                     "disclaimer": 'null',
                     "price": {
                       "__typename": "FormattedMoney",
                       "formatted": "$1,444",
                       "accessibilityLabel": "The price is $1,444"
                     },
                     "role": "LEAD"
                   }
                 ]
               },
               {
                 "__typename": "PriceDisplayMessage",
                 "lineItems": [
                   {
                     "__typename": "LodgingEnrichedMessage",
                     "accessibilityLabel": 'null',
                     "mark": 'null',
                     "state": 'null',
                     "value": "$24,256 total",
                     "badge": 'null'
                   }
                 ]
               },
               {
                 "__typename": "PriceDisplayMessage",
                 "lineItems": [
                   {
                     "__typename": "LodgingEnrichedMessage",
                     "accessibilityLabel": 'null',
                     "mark": 'null',
                     "state": 'null',
                     "value": "includes taxes & fees",
                     "badge": 'null'
                   }
                 ]
               }
             ],
             "strikeOutType": "STANDALONE",
             "priceMessages": [
               {
                 "__typename": "LodgingPlainMessage",
                 "value": "per night"
               }
             ]
           },
           "priceAfterLoyaltyPointsApplied": {
             "__typename": "PropertyPrice",
             "options": [
               {
                 "__typename": "PropertyPriceOption",
                 "strikeOut": 'null',
                 "disclaimer": 'null',
                 "formattedDisplayPrice": "$1,444"
               }
             ],
             "lead": {
               "__typename": "Money",
               "amount": 1443.822857,
               "currencyInfo": {
                 "__typename": "Currency",
                 "code": "USD",
                 "symbol": "$"
               },
               "formatted": "$1,444"
             }
           },
           "propertyFees": [],
           "reviews": {
             "__typename": "PropertyReviewsSummary",
             "score": 9.8,
             "total": 915
           },
           "sponsoredListing": 'null',
           "star": 'null',
           "supportingMessages": 'null',
           "regionId": "2114",
           "priceMetadata": {
             "__typename": "PropertyPriceMetadata",
             "discountType": 'null',
             "rateDiscount": 'null',
             "totalDiscountPercentage": 'null'
           },
           "saveTripItem": 'null'
         }
       ],
       "propertySearchListings": [
         {
           "__typename": "LodgingCard"
         },
         {
           "__typename": "Property",
           "id": "3849185",
           "featuredMessages": [],
           "name": "Corinthia London",
           "availability": {
             "__typename": "PropertyAvailability",
             "available": 'true',
             "minRoomsLeft": 3
           },
           "propertyImage": {
             "__typename": "PropertyImage",
             "alt": "",
             "fallbackImage": 'null',
             "image": {
               "__typename": "Image",
               "description": "Terrace/patio",
               "url":
 "https://images.trvl-media.com/lodging/4000000/3850000/3849200/3849185/70fa8edb.jpg?impolicy=resizecrop&rw=455&ra=fit"
             },
             "subjectId": 22007
           },
           "destinationInfo": {
             "__typename": "PropertyDestinationInfo",
             "distanceFromDestination": {
               "__typename": "Distance",
               "unit": "MILE",
               "value": 0.15
             },
             "distanceFromMessaging": 'null',
             "regionId": "2114"
           },
           "legalDisclaimer": 'null',
           "listingFooter": 'null',
           "mapMarker": {
             "__typename": "MapMarker",
             "label": "$1,444",
             "latLong": {
               "__typename": "Coordinates",
               "latitude": 51.50684,
               "longitude": -0.12435
             }
           },
           "neighborhood": {
             "__typename": "Region",
             "name": "City of Westminster"
           },
           "offerBadge": {
             "__typename": "OfferBadge",
             "primary": {
               "__typename": "Badge",
               "text": "VIP Access",
               "theme_temp": "VIP",
               "icon_temp": 'null',
               "mark": 'null'
             },
             "secondary": 'null'
           },
           "offerSummary": {
             "__typename": "OfferSummary",
             "messages": [
               {
                 "__typename": "OfferSummaryMessage",
                 "message": "Fully refundable",
                 "theme": "SUCCESS",
                 "type": "FREE_CANCEL",
                 "mark": 'null'
               },
               {
                 "__typename": "OfferSummaryMessage",
                 "message": "Reserve now, pay later",
                 "theme": "SUCCESS",
                 "type": "PAY_LATER",
                 "mark": 'null'
               },
               {
                 "__typename": "OfferSummaryMessage",
                 "message": "Collect stamps",
                 "theme": 'null',
                 "type": "LOYALTY_EARN",
                 "mark": {
                   "__typename": "Mark",
                   "id": "loyalty",
                   "token": "mark__loyalty",
                   "description": "loyalty logo"
                 }
               }
             ],
             "attributes": [
               {
                 "__typename": "OfferAttribute",
                 "type": "FREE_CANCELLATION"
               },
               {
                 "__typename": "OfferAttribute",
                 "type": "VIP"
               },
               {
                 "__typename": "OfferAttribute",
                 "type": "PAYMENT_CHOICE"
               }
             ]
           },
           "pinnedDetails": 'null',
           "price": {
             "__typename": "PropertyPrice",
             "options": [
               {
                 "__typename": "PropertyPriceOption",
                 "strikeOut": 'null',
                 "disclaimer": 'null',
                 "formattedDisplayPrice": "$1,444"
               }
             ],
             "priceMessaging": 'null',
             "lead": {
               "__typename": "Money",
               "amount": 1443.822857,
               "currencyInfo": {
                 "__typename": "Currency",
                 "code": "USD",
                 "symbol": "$"
               },
               "formatted": "$1,444"
             },
             "strikeOut": 'null',
             "displayMessages": [
               {
                 "__typename": "PriceDisplayMessage",
                 "lineItems": [
                   {
                     "__typename": "DisplayPrice",
                     "disclaimer": 'null',
                     "price": {
                       "__typename": "FormattedMoney",
                       "formatted": "$1,444",
                       "accessibilityLabel": "The price is $1,444"
                     },
                     "role": "LEAD"
                   }
                 ]
               },
               {
                 "__typename": "PriceDisplayMessage",
                 "lineItems": [
                   {
                     "__typename": "LodgingEnrichedMessage",
                     "accessibilityLabel": 'null',
                     "mark": 'null',
                     "state": 'null',
                     "value": "$24,256 total",
                     "badge": 'null'
                   }
                 ]
               },
               {
                 "__typename": "PriceDisplayMessage",
                 "lineItems": [
                   {
                     "__typename": "LodgingEnrichedMessage",
                     "accessibilityLabel": 'null',
                     "mark": 'null',
                     "state": 'null',
                     "value": "includes taxes & fees",
                     "badge": 'null'
                   }
                 ]
               }
             ],
             "strikeOutType": "STANDALONE",
             "priceMessages": [
               {
                 "__typename": "LodgingPlainMessage",
                 "value": "per night"
               }
             ]
           },
           "priceAfterLoyaltyPointsApplied": {
             "__typename": "PropertyPrice",
             "options": [
               {
                 "__typename": "PropertyPriceOption",
                 "strikeOut": 'null',
                 "disclaimer": 'null',
                 "formattedDisplayPrice": "$1,444"
               }
             ],
             "lead": {
               "__typename": "Money",
               "amount": 1443.822857,
               "currencyInfo": {
                 "__typename": "Currency",
                 "code": "USD",
                 "symbol": "$"
               },
               "formatted": "$1,444"
             }
           },
           "propertyFees": [],
           "reviews": {
             "__typename": "PropertyReviewsSummary",
             "score": 9.8,
             "total": 915
           },
           "sponsoredListing": 'null',
           "star": 'null',
           "supportingMessages": 'null',
           "regionId": "2114",
           "priceMetadata": {
             "__typename": "PropertyPriceMetadata",
             "discountType": 'null',
             "rateDiscount": 'null',
             "totalDiscountPercentage": 'null'
           },
           "saveTripItem": 'null'
         }
       ],
       "summary": {
         "__typename": "PropertyResultsSummary",
         "matchedPropertiesSize": 9143,
         "pricingScheme": {
           "__typename": "PricingScheme",
           "type": "DAILY_RATE"
         },
         "regionCompression": 'null',
         "loyaltyInfo": {
           "__typename": "PropertyLoyaltyDiscount",
           "saveWithPointsMessage": 'null',
           "saveWithPointsActionMessage": 'null'
         },
         "resultsTitleModel": {
           "__typename": "ResultTitleModel",
           "header": "9,143 properties"
         },
         "resultsSummary": [
           {
             "__typename": "LodgingPlainMessage"
           },
           {
             "__typename": "LodgingLinkMessage",
             "accessibilityLabel": "Opens in a new window",
             "value": "What we are paid impacts our sort order",
             "link": {
               "__typename": "LodgingLink",
               "clientSideAnalytics": {
                 "__typename": "ClientSideAnalytics",
                 "linkName": "Sort disclaimer",
                 "referrerId": "HOT.HSR.RecommendedSort.FAQlink"
               },
               "uri": {
                 "__typename": "HttpURI",
                 "value": "https://service.hotels.com/en-us/#/article/19645"
               }
             }
           }
         ]
       },
       "searchCriteria": {
         "__typename": "SearchCriteria",
         "resolvedDateRange": 'null'
       },
       "shoppingContext": {
         "__typename": "ShoppingContext",
         "multiItem": 'null'
       },
       "map": {
         "__typename": "PropertySearchMap",
         "subtitle": 'null'
       },
       "clickstream": {
         "__typename": "SearchClickstreamEvents",
         "searchResultsViewed": 'null'
       }
     }
   }
 })