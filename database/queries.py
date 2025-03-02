user_interaction_query = """
                SELECT 
                    upi.interaction_type,
                    p.product_id,
                    p.product_link,
                    p.prodct_name,
                    p.description,
                    p.category,
                    p.current_price,
                    p.original_price,
                    p.discount_percentage,
                    p.brand,
                    p.availability_status,
                    json_agg(
                        json_build_object(
                            'benefit_type', pcb.benefit_type,
                            'benefit_value', pcb.benefit_value,
                            'valid_until', pcb.valid_until,
                            'card_name', cc.card_name,
                            'bank_name', cc.bank_name
                        )
                    ) FILTER (WHERE pcb.benefit_id IS NOT NULL) as card_benefits
                FROM Users u
                JOIN UserProductInteractions upi ON u.user_id = upi.user_id
                JOIN Products p ON upi.product_id = p.product_id
                LEFT JOIN ProductCardBenefits pcb ON p.product_id = pcb.product_id
                LEFT JOIN CreditCards cc ON pcb.card_id = cc.card_id
                WHERE u.email = $1
                GROUP BY 
                    upi.interaction_type,
                    p.product_id,
                    p.product_link,
                    p.prodct_name,
                    p.description,
                    p.category,
                    p.current_price,
                    p.original_price,
                    p.discount_percentage,
                    p.brand,
                    p.availability_status
                ORDER BY p.product_id
            """
